# 🎮 Rock-Paper-Scissors AI Game

A Python-based Rock-Paper-Scissors game where the computer opponent actually **learns your patterns** and tries to predict your next move. The more you play, the smarter it gets!

---

## 🧠 How the AI Works

This is not just a random computer opponent. The AI inside uses two basic machine learning ideas working together:

**1. Markov Chain Modeling**
The AI keeps track of which move you tend to play after each previous move. For example, if it notices you play `rock` a lot after `scissors`, it will start predicting `rock` next time you play scissors — and then it plays `paper` to beat you.

**2. Frequency-Based Prediction**
The AI also counts which move you use the most overall across the whole game. If you heavily favor one move, the AI will figure that out and counter it.

Both predictions are combined randomly, and the AI always plays the move that would beat its prediction. The randomness factor changes depending on difficulty level.

---

## 📁 Project Structure

```
Rock-Paper-Scissors/
│
├── main.py          # Run this for terminal/text mode
├── gui.py           # Run this for graphical window mode
├── game.py          # Core game rules and score tracking
├── ai_model.py      # The AI brain (Markov + frequency prediction)
├── config.py        # Difficulty level settings
├── stats.py         # Statistics module (in progress)
└── README.md        # This file
```

---

## 🚀 How to Run

### Requirements
- Python 3.x (no external libraries needed for basic version)
- Tkinter (usually comes with Python by default)

### Terminal Mode
```bash
python main.py
```
You'll get a simple numbered menu in the terminal. Choose 1, 2, or 3 to pick a move, 4 to see stats, and 5 to quit.

### GUI Mode (Graphical Window)
```bash
python gui.py
```
A window opens with clickable Rock / Paper / Scissors buttons. The AI's current prediction is shown at the top and updates after every round.

---

## ⚙️ Difficulty Levels

There are four difficulty levels defined in `config.py`:

| Level | Randomness | Starts Learning After |
|-------|------------|----------------------|
| Easy | 50% random moves | 8 games |
| Medium | 20% random moves | 5 games |
| Hard | 10% random moves | 3 games |
| Expert | 5% random moves | 2 games |

At **Easy**, the AI plays randomly half the time — basically a fair opponent.
At **Expert**, it almost never plays randomly and starts learning from round 2.

---

## 🎯 Features

- ✅ Two play modes — terminal and graphical GUI
- ✅ AI that genuinely learns your move patterns
- ✅ Real-time AI prediction display (GUI mode)
- ✅ Score tracking — your wins, AI wins, and ties
- ✅ Win percentage calculator
- ✅ Reset game option that also clears AI memory
- ✅ Four difficulty levels
- ✅ Stats popup with game summary

---

## 🖥️ GUI Preview

The GUI window has:
- A score bar showing `You | AI | Ties` at the top
- A result area showing the last round's moves with emojis
- Three colored move buttons (Red = Rock, Blue = Paper, Green = Scissors)
- An AI status label showing what it's currently predicting
- A "View Detailed Stats" button and a "Reset Game" button
## NOTE : put on full screen window for better experience

---

## 📊 Tech Used

| Technology | What It's Used For |
|------------|-------------------|
| Python 3 | Main programming language |
| Tkinter | Graphical user interface |
| `collections.defaultdict` | Storing Markov transition data |
| `collections.Counter` | Frequency counting of player moves |

---

## 🤔 Known Issues / Bugs

- `main.py` calls `get_ai_move_with_randomness()` but the method in `ai_model.py` is named `get_ai_move()` — terminal mode will crash on the first round. Fix: rename the method call in `main.py`.
- `stats.py` is currently an empty file — stats features are planned but not yet implemented.
- `gui.py` defines the `play()` method twice — only the second definition actually runs, the first one is ignored. Should be cleaned up.

---

## 💡 What I Learned Building This

- How Markov Chains work and how they can be used for prediction
- How to use Python dictionaries to store and retrieve structured data
- Basics of Tkinter for building a GUI without any external libraries
- Why splitting code into separate files (modular design) makes debugging easier
- How even a simple statistical approach counts as a real machine learning technique

---

## 🔮 Planned Improvements

- Fix the bugs mentioned above
- Implement full pattern-length Markov chain (look at sequences of 2–5 past moves)
- Add a round history panel in the GUI showing last 10 moves
- Save and load AI learning data using a JSON file
- Add sound effects using the paths already defined in config.py
- Complete the stats charts using matplotlib
- Create a 3D GUI for Cool and Attractive experience

---

## 👨‍💻 Author

**Raag Shri**  
B.Tech First Year | School of Computing Science Engineering and Artificial Intelligence  
Roll No: 25BAI10431 | Batch: 2025-29 |
VIT Bhopal University

---

## 📄 License

This project was built for educational purposes as part of VITyarthi Course Project.  
Feel free to use or modify it for learning.
