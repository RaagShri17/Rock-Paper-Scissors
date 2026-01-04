# main.py
from game import RPSGame
from ai_model import RPS_AI

def main():
    game = RPSGame()
    ai = RPS_AI()
    
    print("=" * 50)
    print("🎮 ROCK-PAPER-SCISSORS AI GAME 🎮")
    print("=" * 50)
    print("\nThe AI will learn your patterns and try to beat you!")
    print("Can you outsmart the AI?\n")
    
    while True:
        # Get player input
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. View Stats")
        print("5. Quit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '5':
            print("\n👋 Thanks for playing!")
            break
        
        if choice == '4':
            stats = game.get_stats()
            print("\n" + "=" * 30)
            print("📊 GAME STATISTICS")
            print("=" * 30)
            print(f"Your Wins: {stats['player_score']}")
            print(f"AI Wins: {stats['ai_score']}")
            print(f"Ties: {stats['ties']}")
            print(f"Total Games: {stats['total_games']}")
            if stats['total_games'] > 0:
                win_rate = (stats['player_score'] / stats['total_games']) * 100
                print(f"Your Win Rate: {win_rate:.1f}%")
            continue
        
        # Convert choice to move
        move_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        if choice not in move_map:
            print("❌ Invalid choice! Try again.")
            continue
        
        player_move = move_map[choice]
        
        # AI makes its move
        ai_move = ai.get_ai_move_with_randomness(game.player_history, game)
        
        # Play round
        result = game.play_round(player_move, ai_move)
        
        # Display results
        print("\n" + "-" * 30)
        print(f"You chose: {player_move.upper()} ✊📄✂️"[{'rock': 0, 'paper': 1, 'scissors': 2}[player_move]])
        print(f"AI chose: {ai_move.upper()} ✊📄✂️"[{'rock': 0, 'paper': 1, 'scissors': 2}[ai_move]])
        
        if result == "player":
            print("🎉 YOU WIN!")
        elif result == "ai":
            print("🤖 AI WINS!")
        else:
            print("🤝 IT'S A TIE!")
        
        print(f"Score - You: {game.player_score} | AI: {game.ai_score}")
        print("-" * 30)

if __name__ == "__main__":
    main()