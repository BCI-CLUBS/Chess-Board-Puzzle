import piece_movement

# chess board size
BOARD_SIZE = 8
# on the chess board, letters go from left to right, numbers go bottom to top
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# make 2d array of board
currentBoard = [['F' for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]

# p is pawn, r is rook, k is knight, b is bishop, k is king, and q is queen
# entering pieces must format like so: q d2
while True:
    print()
    raw = input("Where do you want a piece?\n")

    if raw.lower() == "stop":
        break
    else:
        # process piece and position
        piece = raw[0].upper()
        x_pos = raw[2].lower()
        x_pos = LETTERS.index(x_pos)
        y_pos = 8 - int(raw[3])
        # set piece into tile
        currentBoard[y_pos][x_pos] = piece

# time to run thru every tile and look for pieces
for y in range(len(currentBoard)):
    for x in range(len(currentBoard[y])):
        if currentBoard[y][x] != 'F' or currentBoard[y][x] != 'T':
            if currentBoard[y][x] == 'R':
                piece_movement.simulateRook(x, y, currentBoard)

print()
# time to run thru every tile and print the board
for y in range(len(currentBoard)):
    for x in range(len(currentBoard[y])):
        print(currentBoard[y][x], end=' ')
    print()

print()
print('peeka boo')