def player(prev_play, opponent_history=[]):
    # 1. Reset state completely when a new 1000-game match starts
    if prev_play == "":
        opponent_history.clear()
        player.play_order = {}
    else:
        opponent_history.append(prev_play)

    # Initialize the memory dictionary if it doesn't exist yet
    if not hasattr(player, "play_order"):
        player.play_order = {}

    # Optimal window size for tracking the opponent's sequences
    n = 5
    
    # Base fallback move for the first few rounds
    guess = "S"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # 2. Update our Markov Chain with the opponent's latest sequence
    if len(opponent_history) > n:
        # Get the sequence of the last n+1 moves
        last_sequence = "".join(opponent_history[-(n+1):])
        player.play_order[last_sequence] = player.play_order.get(last_sequence, 0) + 1

    # 3. Predict their next move based on their current n-length sequence
    if len(opponent_history) >= n:
        current_sequence = "".join(opponent_history[-n:])
        
        # Generate the 3 theoretical sequences that could happen next
        potentials = [
            current_sequence + "R", 
            current_sequence + "P", 
            current_sequence + "S"
        ]
        
        # Look up which of these 3 sequences we have seen most frequently
        sub_order = {k: player.play_order.get(k, 0) for k in potentials}
        
        # Find the max frequency and extract the last character (their predicted move)
        predicted_move = max(sub_order, key=sub_order.get)[-1]
        
        # Counter their predicted move
        guess = ideal_response[predicted_move]

    return guess