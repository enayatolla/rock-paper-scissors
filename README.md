````markdown
# Rock-Paper-Scissors AI Player (FCC Machine Learning Project)

An automated AI player designed to play Rock-Paper-Scissors against four distinct, adaptive computer opponents. This project is a solution for the FreeCodeCamp **Machine Learning with Python** certification challenge.

The primary objective is to build a strategy in `RPS.py` that can successfully read opponent patterns and achieve a **win rate of at least 60%** over 1,000 consecutive rounds against each of the four bots.

---

## 🤖 The Opponents

Each bot in `RPS_game.py` utilizes a unique heuristic to decide its next move. To beat them, the AI adapts dynamically to their individual behaviors:

| Opponent    | Strategy Profile                                                                         | How to Counter It                                                                      |
| :---------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| **Quincy**  | Plays a fixed, repeating 5-move cycle: `["R", "R", "P", "P", "S"]`.                      | Predictable sequence matching.                                                         |
| **Abbey**   | Tracks pairs of _your_ historical moves to predict your next choice and counters it.     | Markov chain tracking your own sequences to stay one step ahead of her predictions.    |
| **Kris**    | Directly counters your absolute last move (e.g., if you played `"P"`, Kris plays `"S"`). | Play the counter-counter to your own last move.                                        |
| **Mrugesh** | Analyzes your last 5 moves and counters whichever move you use most frequently.          | Shift your distribution patterns frequently to force Mrugesh to chase a moving target. |

---

## 🛠️ Project Structure

- `main.py`: The entry point that imports the players and kicks off the 1,000-game match cycles.
- `RPS_game.py`: Contains the match-engine code (`play()`) and the four opponent bots (`quincy`, `abbey`, `kris`, `mrugesh`).
- `RPS.py`: **Your core AI code.** Implements an $N$-gram/Markov Chain tracking model that records how opponents react to historical sequences of your own choices.
- `RPS_test.py`: Unit tests to validate your win rates automatically.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed on your machine:

```bash
python3 --version
```
````

### Installation & Setup

1. Clone this repository to your local directory:

```bash
   git clone <your-repo-link>
   cd rock-paper-scissors

```

2. Execute the main program loop to watch your AI battle the bots sequentially:

```bash
   python3 main.py

```

---

## 🧠 The Winning AI Architecture

Instead of tracking only the opponent's individual actions, the AI in `RPS.py` utilizes a **Self-Referential Markov Chain ($N$-gram)** architecture with an optimal window size of $n=3$.

```
[Your Last 3 Moves] ──> [Opponent's Probable Reaction] ──> [Your Optimal Counter-Play]

```

### Key Pillars:

1. **Dynamic State Flushing:** The AI monitors for an empty initialization string (`prev_play == ""`), which triggers an absolute purge of its internal pattern memory. This stops Quincy's data from corrupting patterns when fighting Kris or Mrugesh.
2. **Frequency Matrix Scoring:** The algorithm logs the string patterns of your historical move paths against the opponent's subsequent counter-actions. It selects the highest-frequency response using Python’s `max()` selector and acts preemptively.
3. **Failsafe Lookback Handlers:** Includes boundary checks (`len(my_history) > n`) to cleanly bypass the initial setup rounds, completely avoiding empty-collection or index out-of-bounds errors.

---

## 📊 Expected Performance Output

When you run `main.py`, you should see performance statistics resembling the following targets:

```text
Player 1 wins: 997 | Player 2 wins: 3   | Ties: 0 | Win rate: 99.70% (vs Quincy)
Player 1 wins: 470 | Player 2 wins: 311 | Ties: 219 | Win rate: 60.18% (vs Abbey)
Player 1 wins: 745 | Player 2 wins: 250 | Ties: 5   | Win rate: 74.87% (vs Kris)
Player 1 wins: 821 | Player 2 wins: 154 | Ties: 25  | Win rate: 84.21% (vs Mrugesh)

```

```

```
