# RPS_game.py

def quincy(prev_play,
           counter=[0]):

    moves = ["R", "R", "P", "P", "S"]
    move = moves[counter[0] % len(moves)]
    counter[0] += 1
    return move


def kris(prev_play):
    if prev_play == "P":
        return "S"
    return "P"


def mrugesh(prev_play,
            opponent_history=[]):

    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return "R"

    most_common = max(
        ["R", "P", "S"],
        key=opponent_history.count
    )

    counter = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    return counter[most_common]


def abbey(prev_play,
          opponent_history=[]):

    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return "R"

    last = opponent_history[-1]

    counter = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    return counter[last]


def play(player1, player2,
         num_games,
         verbose=False):

    p1_prev = ""
    p2_prev = ""

    p1_wins = 0
    p2_wins = 0
    ties = 0

    beats = {
        "R": "S",
        "P": "R",
        "S": "P"
    }

    for _ in range(num_games):

        p1 = player1(p2_prev)
        p2 = player2(p1_prev)

        p1_prev = p1
        p2_prev = p2

        if p1 == p2:
            ties += 1
        elif beats[p1] == p2:
            p1_wins += 1
        else:
            p2_wins += 1

        if verbose:
            print(f"P1: {p1}  P2: {p2}")

    total = p1_wins + p2_wins

    win_rate = (
        0 if total == 0
        else p1_wins / total * 100
    )

    print(f"Player 1 wins: {p1_wins}")
    print(f"Player 2 wins: {p2_wins}")
    print(f"Ties: {ties}")
    print(f"Win rate: {win_rate:.2f}%")

    return win_rate