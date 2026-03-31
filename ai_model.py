import random
from collections import defaultdict, Counter

class RPS_AI:
    def __init__(self):
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.last_move = None
        self.randomness = 0.2  # controls unpredictability

    def update_model(self, player_move):
        if self.last_move:
            self.transitions[self.last_move][player_move] += 1
        self.last_move = player_move

    def predict_next_move(self):
        if not self.last_move:
            return random.choice(['rock', 'paper', 'scissors'])

        next_moves = self.transitions[self.last_move]
        if not next_moves:
            return random.choice(['rock', 'paper', 'scissors'])

        return max(next_moves, key=next_moves.get)

    def frequency_based(self, history):
        if not history:
            return random.choice(['rock', 'paper', 'scissors'])
        return Counter(history).most_common(1)[0][0]

    def get_ai_move(self, player_history, game):
        markov_pred = self.predict_next_move()
        freq_pred = self.frequency_based(player_history)

        predicted = random.choice([markov_pred, freq_pred])

        if random.random() < self.randomness:
            return random.choice(game.moves)

        return game.get_counter_move(predicted)
