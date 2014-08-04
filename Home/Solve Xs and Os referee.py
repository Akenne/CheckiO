"""
You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. 
Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D"
"""
# brute force!@!@
def checkio(game_result):
    for i in game_result:
        if i.count('O') == 3:
            return "O"
        if i.count('X') == 3:
            return "X"
    if game_result[0][0] == game_result[1][0] == game_result[2][0] and game_result[0][0] != ".":
        return game_result[0][0]
    if game_result[0][1] == game_result[1][1] == game_result[2][1] and game_result[0][1] != ".":
        return game_result[0][1]
    if game_result[0][2] == game_result[1][2] == game_result[2][2] and game_result[0][2] != ".":
        return game_result[0][2]
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != ".":
        return game_result[0][0]
    if game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] != ".":
        return game_result[0][2]
    return "D"

checkio([
        "OOX",
        "XXO",
        "OXX"])