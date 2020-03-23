# This problem was asked by Microsoft.

# You have an N by N board. Write a function that, given N, returns the number of possible
# arrangements of the board where N queens can be placed on the board without threatening
# each other, i.e. no two queens share the same row, column, or diagonal.


def n_queens(n, board=[]):
    if n == len(board):
        return 1

    count = 0
    for col in range(n):
        # Add a queen to the board
        board.append(col)

        # Test if this new queen has generated a valid board
        if is_valid(board):
            count += n_queens(n, board)
            print(count)

        board.pop()

    return count


def is_valid(board):
    current_queen_row = len(board) - 1
    current_queen_col = board[-1]

    # Iterate over all already-placed queens and check if any of them can attack
    # each other.
    # - each row is the index (from enumerate) this is because each queen is in a separate row
    for row, col in enumerate(board[:-1]):
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False
    return True


print(n_queens(4))