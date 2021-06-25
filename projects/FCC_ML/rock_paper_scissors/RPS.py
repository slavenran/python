# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
# import random

def player(prev_play, opponent_history=[], opponent_moves = {}):

    COUNTERS = {"R": "P", "S": "R", "P": "S"}   # immutable dict of counter plays based on predicted opponent move
    ROW = 6                                     # number of opponent moves we take as a base to predict

    # starting point when no info given
    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < ROW: return "R"

    # just a nifty thing to shorten our list by dumping outdated moves
    if len(opponent_history) > ROW+1:
        opponent_history.pop(0)
    
    # makes a string from last 5 opponent moves, ops stands for opponent_play_sequence
    ops = "".join(opponent_history)

    # gives weight to 5-character opponent moves inside a dictionary
    opponent_moves[ops] = opponent_moves.get(ops, 0) + 1

    # cuts the first character, makes a list of possible cases and checks which one of them has the highest chance of occurring
    ops = "".join(opponent_history[-ROW:])
    possible = [ops+"R", ops+"P", ops+"S"]
    prediction = max(possible, key=lambda key: opponent_moves.get(key, 0))
    
    # takes the last character from predicter sequence and counters it
    guess = COUNTERS[prediction[-1]]

    return guess


# def player(prev_play, opponent_history=[], my_prev_play=[]):
#     opponent_history.append(prev_play)

#     counter_plays = {"R": "P", "S": "R", "P": "S"}

#     guess = "S"
#     result = ""

#     if len(my_prev_play) > 1:
#         if (prev_play == "R" and my_prev_play[-1] == "P") or (prev_play == "P" and my_prev_play[-1] == "S") or (prev_play == "S" and my_prev_play[-1] == "R"):
#             result = "win"
#         elif (prev_play == "R" and my_prev_play[-1] == "S") or (prev_play == "P" and my_prev_play[-1] == "R") or (prev_play == "S" and my_prev_play[-1] == "P"):
#             result = "lose"
#         else: result = "tie"

#     if result == "win":
#         guess = counter_plays[my_prev_play[-1]]
#     elif result == "lose":
#         guess = counter_plays[prev_play]

#     my_prev_play.append(guess)
#     return guess


# def player(prev_play, opponent_history=[], my_prev_play=[]):
#     opponent_history.append(prev_play)

#     counter_plays = {"R": "P", "S": "R", "P": "S"}

#     # if len(my_prev_play) > 0:
#     #     print(prev_play, my_prev_play[-1])

#     if len(opponent_history) > 4:
#         rs = opponent_history[-5:].count("R")
#         ps = opponent_history[-5:].count("P")
#         ss = opponent_history[-5:].count("S")
#         all_tots = {"R": rs, "P": ps, "S": ss}
#         guess = counter_plays[max(all_tots, key=all_tots.get)]
#         opponent_history.pop(0)
#     else:
#         guess = ["R", "S", "P"]
#         guess = guess[random.randrange(3)]
    
#     # my_prev_play.append(guess)
#     return guess
