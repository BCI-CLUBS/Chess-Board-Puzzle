# lets simulate where the pieces CAN go

def simulateRook(x, y, board):
    # Move up
    for i in range(y-1, -1, -1):
        if checkTile(i, x, board):
            break
    # Move down
    for i in range(y+1, 8):
        if checkTile(i, x, board):
            break
    # Move Right
    for i in range(x+1, 8):
        if checkTile(y, i, board):
            break
    # Move Right
    for i in range(x-1, -1, -1):
        if checkTile(y, i, board):
            break

def simulateKnight(x, y, board):
	# Knight moves in L shape, so 3 then 2, or 2 then 3.
	# thereby a combination of 3 in a direction, then 2 in a direction, or vice versa
	threeLong = [-3, 3]
	twoLong = [-2, 2]

# if the tile that we are simulating movement into
# has something in it, we cant go into it
# will return true, if something on tile (that isnt T or F)
def checkTile(y, x, board):
    if board[y][x] == 'F':
        board[y][x] = 'T'
        return False
    else:
        if board[y][x] != 'T':
            return True