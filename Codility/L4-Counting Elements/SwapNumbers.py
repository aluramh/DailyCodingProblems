def counting(A, m):
    """
    Creates an array with the counts of the array
    """
    n = len(A)
    count = [0] * (m + 1)

    for k in range(n):
        count[A[k]] += 1

    return count


def can_be_swapped(A, B, m):
    # n = len(A)
    max_possible_val = m
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a

    # If this is a fraction, it's not possible since it's just ints
    if d % 2 // 1:
        return False

    d = d // 2

    # Count the numbers in A
    # O(n)
    count = counting(A, max_possible_val)

    # Loop through B and assume that we will swap it with a value from A
    for num in B:
        # For this num from B, we would require "target_elem" in A to be
        # present. This is the difference between the sum of both arrays.
        # becuase 1 array will increase and the other has to decrease.
        target_elem = num - d

        # Check if the target element we are looking for is a positive number
        is_positive_integer = 0 <= target_elem

        # Check also that it is within constraints; less than m, which is the
        # max possible value
        is_within_constraints = target_elem <= max_possible_val

        # Finally, check that it IS present in the array A, by looking if the
        # count of that value in array A is greater than 0
        is_present = count[target_elem] > 0 if target_elem <= len(B) else None

        if is_positive_integer and is_within_constraints and is_present:
            print(f"Swap {target_elem} for {num}")
            return True

    return False


if __name__ == "__main__":
    try:
        tests = [
            ([3, 4, 3], [4, 1, 1], 4, True),
        ]

        for A, B, m, expected_result in tests:
            result = can_be_swapped(A, B, m)
            print(result)
            assert result == expected_result

    except AssertionError as e:
        print("AssertionError", e)
