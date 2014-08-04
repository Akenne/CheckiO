"""
A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. 
With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.
"""

def safe_pawns(pawns):
    ct = 0
    for i in pawns:
        if str(chr(ord(i[0]) - 1) + str(int(str(i)[1])-1)) in pawns or str(chr(ord(i[0]) + 1) + str(int(str(i)[1])-1)) in pawns:
            ct +=1
    return ct