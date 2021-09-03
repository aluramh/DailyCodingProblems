from typing import List, Tuple


def main(matrix: List[int], target: int):
    def getFlatIndexValue(i: int) -> int:
        nonlocal rows, cols, size

        # Get the row
        x = i // cols

        # Get the number of items from the previous rows you skipped
        numbers_to_decrease = (x * cols)
        # Subtract that number of items from the current index you are at to get the [col]
        y = i - numbers_to_decrease

        return matrix[x][y]

    def binaryMatrixSearch(matrix: List[int], target: int, low: int,
                           high: int) -> bool:
        nonlocal rows, cols, size

        if high < low:
            return False

        mid_index = low + (high - low) // 2

        # Convert the mid_index to a matrix (x,y) index
        mid = getFlatIndexValue(mid_index)

        if mid == target:
            return True
        elif mid < target:
            return binaryMatrixSearch(matrix, target, mid_index + 1, high)
        elif mid > target:
            return binaryMatrixSearch(matrix, target, low, mid_index - 1)

    rows = len(matrix)
    cols = len(matrix[0])
    size = rows * cols
    return binaryMatrixSearch(matrix, target, 0, size - 1)


# TESTS

tests = [
    ([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ], 30, True),
    ([
        [-8, -8, -7, -7, -6, -5, -3, -2],
        [0, 0, 1, 3, 4, 6, 8, 8],
        [11, 12, 14, 16, 18, 18, 19, 19],
        [22, 23, 25, 27, 28, 30, 30, 31],
        [34, 35, 37, 39, 40, 42, 43, 45],
        [48, 50, 51, 51, 53, 54, 55, 57],
        [58, 60, 62, 62, 62, 63, 63, 65],
        [68, 69, 71, 72, 72, 72, 74, 76],
    ], 76, True),
    ([[1]], 0, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 6, False),
]

for (matrix, target, result) in tests:
    try:
        r = main(matrix, target)
        assert (r == result)
    except AssertionError as e:
        print("Error!")
        exit()

print("Finished")
