# lets simulate where the pieces CAN go

def simulateRook(x, y, board, size):
    # this is spaghti code

    # Move up
    for i in range(y-1, -1, -1):
        if checkTile(i, x, board):
            break
    # Move down
    for i in range(y+1, size):
        if checkTile(i, x, board):
            break
    # Move Right
    for i in range(x+1, size):
        if checkTile(y, i, board):
            break
    # Move Right
    for i in range(x-1, -1, -1):
        if checkTile(y, i, board):
            break


def simulateKnight(x, y, board, size):
    # Knight moves in L shape, so 3 then 2, or 2 then 3.
    # thereby a combination of 3 in a direction, then 2 in a direction, or vice versa
    # this is spaghti code
    threeLong = [-2, 2]
    twoLong = [-1, 1]

    # Offset three horizontaly and 2 vertically
    for i in threeLong:
        if i+x < size and i+x >= 0:
             for j in twoLong:
                 if j+y < size and j+y >= 0:
                     checkTile(j+y, i+x, board)

    # Now other way
    for i in twoLong:
        if i+x < size and i+x >= 0:
             for j in threeLong:
                 if j+y < size and j+y >= 0:
                     checkTile(j+y, i+x, board)


def simulateBishop(x, y, board, size):
    # Keep offseting by one, and make sure we're in bound
    # this is spaghti code

    # up right
    for i in range(1, size):
        if y-i < size and x+i < size:
            if y-i >= 0 and x+i >= 0:
                if checkTile(y-i, x+i, board):
                    break
    # down right
    for i in range(1, size):
        if y+i < size and x+i < size:
            if y+i >= 0 and x+i >= 0:
                if checkTile(y+i, x+i, board):
                    break
    # down left
    for i in range(1, size):
        if y+i < size and x-i < size:
            if y+i >= 0 and x-i >= 0:
                if checkTile(y+i, x-i, board):
                    break
    # down right
    for i in range(1, size):
        if y-i < size and x-i < size:
            if y-i >= 0 and x-i >= 0:
                if checkTile(y-i, x-i, board):
                    break


# if the tile that we are simulating movement into
# has something in it, we cant go into it
# will return true, if something on tile (that isnt T or F)


def checkTile(y, x, board):
    if board[y][x] == 'F' or board[y][x] == 'T':
        board[y][x] = 'T'
        return False
    else:
        return True