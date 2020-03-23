from numpy import matrix


class SudokuSolver:
    board = None
    moves = []
    solutions_count = 0

    def __init__(self, board):
        self.board = board

    def generate_random_board(self):
        pass

    def print_board(self):
        print(matrix(self.board))

    def possible_move(self, x, y, n):
        # check in x row
        for i in range(9):
            if self.board[i][y] == n:
                return False

        # check in y column
        for j in range(9):
            if self.board[x][j] == n:
                return False

        # check in square. first calculate offsets for the 3x3 squares
        init_x = x // 3 * 3
        init_y = y // 3 * 3

        for i in range(init_x, init_x + 3):
            for j in range(init_y, init_y + 3):
                if self.board[i][j] == n:
                    return False

        return True

    def solve(self):
        # go through the whole grid
        for x in range(9):
            for y in range(9):
                # if this spot is empty
                if self.board[x][y] == 0:
                    # find a number that fits here
                    for n in range(1, 10):
                        if self.possible_move(x, y, n):
                            self.board[x][y] = n
                            self.moves.append({"x": x, "y": y, "num": n})
                            self.solve()  # keep finding numbers...

                            # backtrack because we returned here
                            self.board[x][y] = 0

                    # if we've tried every number and nothing works, then
                    # it's a dead-end. we return.
                    return

        # if we're here, we have looped the whole grid and there's nothing more to
        # place in the grid. this means we're finished. print result.
        self.solutions_count += 1

        # save the moves it took
        moves_count = len(self.moves)
        print(moves_count)
        print(self.moves)
        self.moves = []

        # print the board
        self.print_board()


board1 = [[0, 3, 0, 0, 0, 0, 0, 8, 9],
          [0, 1, 0, 7, 0, 0, 0, 3, 4],
          [0, 0, 0, 0, 3, 0, 0, 5, 6],
          [1, 0, 3, 0, 6, 5, 8, 0, 7],
          [0, 0, 0, 8, 1, 0, 0, 0, 2],
          [6, 0, 8, 3, 0, 0, 0, 1, 5],
          [3, 0, 5, 0, 8, 0, 6, 0, 1],
          [8, 6, 0, 5, 0, 0, 0, 7, 3],
          [0, 0, 1, 0, 0, 0, 0, 0, 8]]


board = SudokuSolver(board1)
board.solve()
print("This board has {} solution(s)".format(board.solutions_count))
