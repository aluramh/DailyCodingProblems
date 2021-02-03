# An array A consisting of N different integers is given. The array contains
# integers in the range [1..(N + 1)], which means that exactly one element is
# missing.
# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

# NOTE: - ^^^^^ THIS IS IMPORTANT AS IT TELLS YOU THAT YOU ALWAYS START WITH 1


def partial_sum(n):
    """
    Formula for the partial sum of the sequence which goes to infinity.
    """
    return n * (n + 1) // 2


def solution(A):
    """
    This is the simple solution that solved the codility problem.
    """
    n = len(A) + 1
    expected_sum = partial_sum(n)
    actual_sum = sum(A)
    return expected_sum - actual_sum


def sum_range(start, end):
    """
    O(1) function to calculate the sum of a sequential numbers.
    """
    before_start_sum = partial_sum(start - 1)
    end_sum = partial_sum(end)

    return end_sum - before_start_sum


def solution_2(A):
    """
    Sum from start to end. Sequence numbers only.
    """
    # Need to sort this in order to grab the max and min
    A.sort()

    # Get the start and endpoints of the array
    start = A[0]
    end = A[len(A) - 1]

    # Calculate th expected average and the actual sum and find out the missing number by substracting
    expected_sum = sum_range(start, end)
    actual_sum = sum(A)
    result = expected_sum - actual_sum
    return result


if __name__ == "__main__":
    try:
        tests = [
            ([2, 3, 1, 5], 4),
            ([3, 1, 4, 2], 0),
            ([9, 5, 7, 8], 6),
            ([20, 26, 14, 15, 12, 17, 21, 18, 19, 25, 23, 24, 13, 16], 22),
        ]

        for A, expected_result in tests:
            result = solution_2(A)
            print(result)
            assert result == expected_result
            

    except AssertionError as e:
        print("AssertionError", e)