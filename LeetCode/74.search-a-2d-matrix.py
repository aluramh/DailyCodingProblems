from typing import List


def main(matrix, target):
    def binarySearchRows(
        matrix: List[List[int]],
        target: int,
        low: int,
        high: int,
    ) -> int:
        """
        This function is equivalent of finding the right-most
        less-than-or-equal value in a list made up of the first
        items of each row.
        """
        nonlocal min_range

        if high < low:
            return min_range

        mid_index = low + (high - low) // 2
        mid = matrix[mid_index][0]  # Because 1 <= n

        if mid == target:
            return mid_index

        elif mid < target:
            # Update the place where we found the left-most mid index to the right
            min_range = mid_index
            return binarySearchRows(matrix, target, mid_index + 1, high)

        elif mid > target:
            return binarySearchRows(matrix, target, low, mid_index - 1)

    def binarySearch(row: List[int], target: int, low: int, high: int) -> bool:
        """
        This is a standard binary search
        """
        if high < low:
            return False

        mid_index = low + (high - low) // 2
        mid = row[mid_index]

        if mid == target:
            return True
        elif mid < target:
            return binarySearch(row, target, mid_index + 1, high)
        elif mid > target:
            return binarySearch(row, target, low, mid_index - 1)

    # MARK: - Logic start

    # Indices
    min_range = None
    max_range = None

    # Initialize range values
    if min_range is None:
        min_range = 0
    if max_range is None:
        max_range = len(matrix)

    target_row_index = binarySearchRows(matrix, target, 0, len(matrix) - 1)
    print(f"Right-most, left-most item: {target_row_index}")

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
