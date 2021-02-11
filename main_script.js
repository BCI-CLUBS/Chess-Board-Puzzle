// making chess board

const BOARD_SIZE = 8;

// create 2d array thats 8 long
var currentBoard = new Array(BOARD_SIZE);

// fill elements of array with arrays to make 2d array
for (var i = 0; i < currentBoard.length; i++) {
    currentBoard[i] = new Array(BOARD_SIZE);

    // fill the 2d array with all false, will be true if piece can go into the tile
    for (var j = 0; j < currentBoard[i].length; j++) {
        currentBoard[i][j] = false;
    }
}