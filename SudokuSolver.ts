interface Move {
  x: number;
  y: number;
  n: number;
}

type Row = [
  number,
  number,
  number,
  number,
  number,
  number,
  number,
  number,
  number
];

type Board = [Row, Row, Row, Row, Row, Row, Row, Row, Row];

const board1: Board = [
  [0, 3, 0, 0, 0, 0, 0, 8, 9],
  [0, 1, 0, 7, 0, 0, 0, 3, 4],
  [0, 0, 0, 0, 3, 0, 0, 5, 6],
  [1, 0, 3, 0, 6, 5, 8, 0, 7],
  [0, 0, 0, 8, 1, 0, 0, 0, 2],
  [6, 0, 8, 3, 0, 0, 0, 1, 5],
  [3, 0, 5, 0, 8, 0, 6, 0, 1],
  [8, 6, 0, 5, 0, 0, 0, 7, 3],
  [0, 0, 1, 0, 0, 0, 0, 0, 8],
];

function possible_move(board: Board, x: number, y: number, n: number) {
  const boardSize = new Array(9).fill(undefined);

  // check in x row
  for (let i = 0; i < boardSize.length; i++) {
    if (board[i][y] == n) {
      return false;
    }
  }

  // check in y column
  for (let j = 0; j < boardSize.length; j++) {
    if (board[x][j] == n) {
      return false;
    }
  }

  // check in square. first calculate offsets for the 3x3 squares
  const init_x = Math.floor(x / 3) * 3;
  const init_y = Math.floor(y / 3) * 3;

  for (let i = init_x; i < init_x + 3; i++) {
    for (let j = init_y; j < init_y + 3; j++) {
      if (board[i][j] == n) {
        return false;
      }
    }
  }

  return true;
}

function solve(board: Board) {
  const boardSize = new Array(9).fill(undefined);
  let moves: Move[] = [];
  let solutions_count = 0;

  function helper() {
    // go through the whole grid
    for (let x = 0; x < boardSize.length; x++) {
      for (let y = 0; y < boardSize.length; y++) {
        // if this spot is empty
        if (board[x][y] == 0) {
          // find a number that fits here
          for (let n = 1; n < boardSize.length + 1; n++) {
            if (possible_move(board, x, y, n) === true) {
              board[x][y] = n;
              moves.push({ x: x, y: y, n: n });
              helper(); // keep finding numbers...

              // backtrack because we returned here
              board[x][y] = 0;
            }
          }

          // if we've tried every number and nothing works, then
          // it's a dead-end. we return.
          return;
        }
      }
    }

    // if we're here, we have looped the whole grid and there's nothing more to
    // place in the grid. this means we're finished. print result.
    solutions_count += 1;

    // save the moves it took
    // let moves_count = moves.length;
    // console.log({ moves_count });
    // console.log({ moves });
    moves = [];

    // print the board
    console.log({ board });
  }

  helper();
  return { board, solutions_count };
}

console.log({ ...solve(board1) });
