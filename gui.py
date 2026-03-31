# GUI interface (optional)
import tkinter as tk
from tkinter import messagebox
from game import RPSGame
from ai_model import RPS_AI
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter

class RPS_GUI:
    def __init__(self):
        self.game = RPSGame()
        self.ai = RPS_AI()
        
        # Create main window
        self.window = tk.Tk()
        self.window.title("🎮 Rock-Paper-Scissors AI")
        self.window.geometry("500x600")
        self.window.configure(bg='#0f172a')
        
        self.create_widgets()

    def ai_thinking(self):
       self.result_label.config(text="🤖 AI is thinking...")
       self.window.update()
    
    def create_widgets(self):
        # Title
        title = tk.Label(
            self.window,
            text="Rock Paper Scissors AI",
            font=("Arial", 24, "bold"),
            bg='#2C3E50',
            fg='white'
        )
        title.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            self.window,
            text="The AI learns your patterns!",
            font=("Arial", 12),
            bg='#2C3E50',
            fg='#ECF0F1'
        )
        subtitle.pack()

        self.ai_label = tk.Label(
            self.window,
            text="🤖 AI Status: Learning...",
            font=("Arial", 12, "bold"),
            bg='#0f172a',
            fg='#00f5ff'
        )
        self.ai_label.pack(pady=10)
        
        # Score display
        self.score_label = tk.Label(
            self.window,
            text=f"You: 0  |  AI: 0  |  Ties: 0",
            font=("Arial", 16, "bold"),
            bg='#34495E',
            fg='white',
            padx=20,
            pady=10
        )
        self.score_label.pack(pady=20)
        
        # Result display
        self.result_label = tk.Label(
            self.window,
            text="Choose your move!",
            font=("Arial", 14),
            bg='#2C3E50',
            fg='#ECF0F1',
            height=3
        )
        self.result_label.pack(pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.window, bg='#2C3E50')
        buttons_frame.pack(pady=20)
        
        # Move buttons
        moves = [
            ("✊ Rock", "rock", "#E74C3C"),
            ("📄 Paper", "paper", "#3498DB"),
            ("✂️ Scissors", "scissors", "#2ECC71")
        ]
        
        for text, move, color in moves:
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 14, "bold"),
                bg=color,
                fg='white',
                width=12,
                height=2,
                command=lambda m=move: self.play(m)
            )
            btn.pack(pady=5)
        
        # Stats button
        stats_btn = tk.Button(
            self.window,
            text="📊 View Detailed Stats",
            font=("Arial", 12),
            bg="#2B0EE7",
            fg='white',
            command=self.show_stats
        )
        stats_btn.pack(pady=10)
        
        # Reset button
        reset_btn = tk.Button(
            self.window,
            text="🔄 Reset Game",
            font=("Arial", 12),
            bg='#E67E22',
            fg='white',
            command=self.reset_game
        )
        reset_btn.pack(pady=5)
    
    def play(self, player_move):
        self.ai_thinking()

    def play(self, player_move):
        self.ai_thinking()
    
        # ✅ Get AI move
        ai_move = self.ai.get_ai_move(self.game.player_history, self.game)
    
        # ✅ Play round
        result = self.game.play_round(player_move, ai_move)
    
        # ✅ VERY IMPORTANT → Update AI learning
        self.ai.update_model(player_move)
    
        # ✅ Prediction display
        prediction = self.ai.predict_next_move()
        self.ai_label.config(text=f"🤖 AI predicts: {prediction.upper()}")
    
        # ✅ Update UI properly
        self.update_display(player_move, ai_move, result)
       
    
    def update_display(self, player_move, ai_move, result):
        # Update score
        stats = self.game.get_stats()
        self.score_label.config(
            text=f"You: {stats['player_score']}  |  AI: {stats['ai_score']}  |  Ties: {stats['ties']}"
        )
        
        # Update result
        move_emoji = {'rock': '✊', 'paper': '📄', 'scissors': '✂️'}
        
        result_text = f"You: {move_emoji[player_move]}  vs  AI: {move_emoji[ai_move]}\n\n"
        
        if result == "player":
            result_text += "🎉 YOU WIN! 🎉"
            self.result_label.config(fg='#2ECC71')
        elif result == "ai":
            result_text += "🤖 AI WINS! 🤖"
            self.result_label.config(fg='#E74C3C')
        else:
            result_text += "🤝 IT'S A TIE! 🤝"
            self.result_label.config(fg='#F39C12')
        
        self.result_label.config(text=result_text)
    
    def show_stats(self):
        stats = self.game.get_stats()
        total = stats['total_games']
        
        if total == 0:
            messagebox.showinfo("Stats", "No games played yet!")
            return
        
        win_rate = (stats['player_score'] / total) * 100
        ai_win_rate = (stats['ai_score'] / total) * 100
        
        msg = f"""
📊 GAME STATISTICS 📊

Total Games: {total}

Your Wins: {stats['player_score']} ({win_rate:.1f}%)
AI Wins: {stats['ai_score']} ({ai_win_rate:.1f}%)
Ties: {stats['ties']}

{'🏆 You are winning!' if stats['player_score'] > stats['ai_score'] else '🤖 AI is winning!' if stats['ai_score'] > stats['player_score'] else '⚖️ Perfectly balanced!'}
        """
        
        messagebox.showinfo("Game Statistics", msg)
    
    def reset_game(self):
        if messagebox.askyesno("Reset Game", "Are you sure you want to reset?"):
            self.game = RPSGame()
            self.ai = RPS_AI()
            self.score_label.config(text="You: 0  |  AI: 0  |  Ties: 0")
            self.result_label.config(text="Choose your move!", fg='#ECF0F1')
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = RPS_GUI()
    app.run()
