# AI prediction logic
import random
from collections import Counter

class RPS_AI:
    def __init__(self):
        self.pattern_length = 3  # Look at last 3 moves
        self.learning_threshold = 5  # Start predicting after 5 games
    
    def find_pattern(self, history):
        """Find most common pattern in player's history"""
        if len(history) < self.learning_threshold:
            # Not enough data, play randomly
            return random.choice(['rock', 'paper', 'scissors'])
        
        # Look at recent pattern
        recent_moves = history[-self.pattern_length:]
        pattern = ''.join([m[0] for m in recent_moves])  # e.g., "rps"
        
        # Search for this pattern in history
        pattern_matches = []
        for i in range(len(history) - self.pattern_length):
            if ''.join([m[0] for m in history[i:i+self.pattern_length]]) == pattern:
                # Found pattern, check what came next
                if i + self.pattern_length < len(history):
                    pattern_matches.append(history[i + self.pattern_length])
        
        if pattern_matches:
            # Predict most common next move after this pattern
            prediction = Counter(pattern_matches).most_common(1)[0][0]
        else:
            # Pattern not found, look at overall frequency
            prediction = Counter(history).most_common(1)[0][0]
        
        return prediction
    
    def predict_and_counter(self, player_history, game):
        """Predict player's move and return counter move"""
        if len(player_history) < self.learning_threshold:
            # Early game: play randomly
            return random.choice(game.moves)
        
        # Predict player's next move
        predicted_move = self.find_pattern(player_history)
        
        # Return counter move
        counter_move = game.get_counter_move(predicted_move)
        
        return counter_move
    
    def get_ai_move_with_randomness(self, player_history, game, randomness=0.2):
        """Add some randomness so AI isn't 100% predictable"""
        if random.random() < randomness:
            # Sometimes play randomly
            return random.choice(game.moves)
        else:
            # Use pattern prediction
            return self.predict_and_counter(player_history, game)
        
class AdvancedAI(RPS_AI):
    def __init__(self):
        super().__init__()
        self.transition_matrix = {}
    
    def update_transition_matrix(self, history):
        """Build move transition probabilities"""
        for i in range(len(history) - 1):
            current = history[i]
            next_move = history[i + 1]
            
            if current not in self.transition_matrix:
                self.transition_matrix[current] = {}
            
            if next_move not in self.transition_matrix[current]:
                self.transition_matrix[current][next_move] = 0
            
            self.transition_matrix[current][next_move] += 1    


# ai_model.py

import random
from collections import Counter
from config import DifficultySettings  # Import difficulty settings

class RPS_AI:
    def __init__(self, difficulty='MEDIUM'):
        """Initialize AI with difficulty level"""
        # Get difficulty settings
        if difficulty == 'EASY':
            settings = DifficultySettings.EASY
        elif difficulty == 'MEDIUM':
            settings = DifficultySettings.MEDIUM
        elif difficulty == 'HARD':
            settings = DifficultySettings.HARD
        elif difficulty == 'EXPERT':
            settings = DifficultySettings.EXPERT
        else:
            settings = DifficultySettings.MEDIUM
        
        # Apply settings
        self.pattern_length = settings['pattern_length']
        self.randomness = settings['randomness']
        self.learning_threshold = settings['learning_threshold']
        self.difficulty = difficulty
    
    def find_pattern(self, history):
        """Find most common pattern in player's history"""
        if len(history) < self.learning_threshold:
            return random.choice(['rock', 'paper', 'scissors'])
        
        recent_moves = history[-self.pattern_length:]
        pattern = ''.join([m[0] for m in recent_moves])
        
        pattern_matches = []
        for i in range(len(history) - self.pattern_length):
            if ''.join([m[0] for m in history[i:i+self.pattern_length]]) == pattern:
                if i + self.pattern_length < len(history):
                    pattern_matches.append(history[i + self.pattern_length])
        
        if pattern_matches:
            prediction = Counter(pattern_matches).most_common(1)[0][0]
        else:
            prediction = Counter(history).most_common(1)[0][0]
        
        return prediction
    
    def predict_and_counter(self, player_history, game):
        """Predict player's move and return counter move"""
        if len(player_history) < self.learning_threshold:
            return random.choice(game.moves)
        
        predicted_move = self.find_pattern(player_history)
        counter_move = game.get_counter_move(predicted_move)
        
        return counter_move
    
    def get_ai_move_with_randomness(self, player_history, game):
        """Add randomness based on difficulty level"""
        if random.random() < self.randomness:
            return random.choice(game.moves)
        else:
            return self.predict_and_counter(player_history, game)
    
    def get_difficulty_name(self):
        """Return current difficulty level"""
        return self.difficulty