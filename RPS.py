def player(prev_play, opponent_history=[]):
    # 1. Reset states completely on a new match
    if prev_play == "":
        opponent_history.clear()
        if hasattr(player, "my_history"):
            player.my_history.clear()
        if hasattr(player, "my_patterns"):
            player.my_patterns.clear()

    # Track opponent history
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize tracking variables on the function object
    if not hasattr(player, "my_history"):
        player.my_history = []
    if not hasattr(player, "my_patterns"):
        player.my_patterns = {}

    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
    
    # Base fallback play
    guess = "R"
    
    # We will look at our own history to see how the opponent responds to our moves
    n = 3

    # 2. Update pattern dictionary based on what the opponent did in response to our past moves
    if len(player.my_history) > n:
        # What did we play over the sequence leading up to their last move?
        past_sequence = "".join(player.my_history[-(n+1):-1])
        last_opponent_response = prev_play
        
        if past_sequence not in player.my_patterns:
            player.my_patterns[past_sequence] = {"R": 0, "P": 0, "S": 0}
        player.my_patterns[past_sequence][last_opponent_response] += 1

    # 3. Predict their next move using our current sequence
    if len(player.my_history) >= n:
        current_sequence = "".join(player.my_history[-n:])
        
        # If we have seen this sequence of our own moves before, see how they usually respond
        if current_sequence in player.my_patterns:
            predicted_move = max(player.my_patterns[current_sequence], key=player.my_patterns[current_sequence].get)
            guess = ideal_response[predicted_move]
        else:
            # Fallback: Counter-counter what we played last round (great against Kris)
            guess = ideal_response[ideal_response[player.my_history[-1]]]

    # Log our guess and send it
    player.my_history.append(guess)
    return guess