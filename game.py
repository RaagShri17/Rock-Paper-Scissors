# Main game logic

import random

class RPSGame:
    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.ai_score = 0
        self.ties = 0
        self.player_history = []
        self.ai_history = []
    
    def determine_winner(self, player_move, ai_move):
        """Determine who wins the round"""
        if player_move == ai_move:
            return "tie"
        
        win_conditions = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        
        if win_conditions[player_move] == ai_move:
            return "player"
        else:
            return "ai"
    
    def get_counter_move(self, predicted_move):
        """Get move that beats the predicted move"""
        counter = {
            'rock': 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
        }
        return counter[predicted_move]
    
    def play_round(self, player_move, ai_move):
        """Play one round and update scores"""
        self.player_history.append(player_move)
        self.ai_history.append(ai_move)
        
        result = self.determine_winner(player_move, ai_move)
        
        if result == "player":
            self.player_score += 1
        elif result == "ai":
            self.ai_score += 1
        else:
            self.ties += 1
        return result
    
    def get_stats(self):
        """Return current game statistics"""
        total_games = self.player_score + self.ai_score + self.ties
        return {
            'player_score': self.player_score,
            'ai_score': self.ai_score,
            'ties': self.ties,
            'total_games': total_games
        }

def analyze_player_tendencies(self):
    """Show which move player uses most"""
    from collections import Counter
    freq = Counter(self.game.player_history)
    return freq.most_common()

def get_counter_move(self, move):
    counter = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }
    return counter[move]
