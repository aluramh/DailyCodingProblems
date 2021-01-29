# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

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


def solution(A):
    pass


if __name__ == "__main__":
    try:
        tests = [
            ([2, 3, 1, 5], 4),
        ]

        for A, expected_result in tests:
            result = solution(expected_result)
            print(result)
            assert result == expected_result

    except AssertionError as e:
        print("AssertionError", e)