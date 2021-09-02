from typing import List


def binarySearchRows(
    matrix: List[List[int]],
    target: int,
    low: int,
    high: int,
    start_index: int = None  # always has to be less than, or equal, target
) -> int:
    if high < low:
        return start_index

    mid_index = low + (high - low) // 2
    mid = matrix[mid_index][0]  # Because 1 <= n

    # print(f"matrix[{mid_index}]: {matrix[mid_index]} => {mid}")
    if start_index is None:
        start_index = mid_index

    if mid == target:
        return mid_index

    elif mid < target:
        next_possible_index = binarySearchRows(matrix, target, mid_index + 1,
                                               high, start_index)

        largest = max(matrix[next_possible_index][0], mid)
        if largest < target:
            return mid_index
        elif matrix[next_possible_index][0] < target:
            return next_possible_index

    elif mid > target:
        next_possible_index = binarySearchRows(matrix, target, low,
                                               mid_index - 1, start_index)

        return min(mid_index, next_possible_index)


def binarySearch(row: List[int], target: int, low: int, high: int) -> bool:
    if high < low:
        return False

    mid_index = low + (high - low) // 2
    mid = row[mid_index]

    # print(f"matrix[{mid_index}]: {row[mid_index]}")

    if mid == target:
        return True
    elif mid < target:
        return binarySearch(row, target, mid_index + 1, high)
    elif mid > target:
        return binarySearch(row, target, low, mid_index - 1)


def main(matrix, target):
    # MARK: - Logic start

    target_row_index = binarySearchRows(matrix, target, 0, len(matrix) - 1)
    print(f"target_row_index: {target_row_index}")

    # Check the next index to see if the item may have been there
    next_index = target_row_index + 1
    if next_index < len(matrix) and matrix[next_index][0] <= target:
        target_row_index = next_index

    # If it returns None, then it could be the last row
    if target_row_index is None:
        print("target_row_index was None")
        return False

    target_row = matrix[target_row_index]
    is_in_matrix = binarySearch(target_row, target, 0, len(target_row) - 1)
    print(f"is_in_matrix: {is_in_matrix}")
    return is_in_matrix


# TESTS

tests = [
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
    # ([[1]], 0, False),
    # ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
]

for (matrix, target, result) in tests:
    try:
        r = main(matrix, target)
        assert (r == result)
    except AssertionError as e:
        print("Error!")
        exit()

print("Finished")
