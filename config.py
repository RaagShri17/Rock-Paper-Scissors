# config.py

class DifficultySettings:
    """Configuration for different AI difficulty levels"""
    
    EASY = {
        'pattern_length': 2,      # Look at last 2 moves
        'randomness': 0.5,        # 50% random moves
        'learning_threshold': 8   # Start learning after 8 games
    }
    
    MEDIUM = {
        'pattern_length': 3,      # Look at last 3 moves
        'randomness': 0.2,        # 20% random moves
        'learning_threshold': 5   # Start learning after 5 games
    }
    
    HARD = {
        'pattern_length': 4,      # Look at last 4 moves
        'randomness': 0.1,        # 10% random moves
        'learning_threshold': 3   # Start learning after 3 games
    }
    
    EXPERT = {
        'pattern_length': 5,      # Look at last 5 moves
        'randomness': 0.05,       # 5% random moves
        'learning_threshold': 2   # Start learning after 2 games
    }

# Sound file paths
SOUNDS = {
    'win': 'sounds/win.wav',
    'lose': 'sounds/lose.wav',
    'tie': 'sounds/tie.wav',
    'click': 'sounds/click.wav'
}