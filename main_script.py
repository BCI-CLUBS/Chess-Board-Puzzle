import piece_movement

# chess board size
BOARD_SIZE = 8
# on the chess board, letter go from left to right, numbers go bottom to top
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# make 2d array of board
currentBoard =  [[False for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]

# p is pawn, r is rook, k is knight, b is bishop, k is king, and q is queen
# entering pieces must format like so: q d2
while True:
    print()
    raw = input("Where do you want a piece?\n")

    if raw == "stop":
        break
    else:
        # process piece and position
        piece = raw[0]
        x_pos = raw[2]
        x_pos = LETTERS.index(x_pos)
        y_pos = int(raw[3]) - 1
        # set piece into tile
        currentBoard[x_pos][y_pos] = piece

# time to test where each piece can move


print()
print('peeka boo')