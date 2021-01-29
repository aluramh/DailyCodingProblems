def solution(A):
    """
    Input: Array of N integers [1...100,000]. Each element is [1...4]
    Output: Min steps to make all elements equal. A step is +/- 1
    """
    def ceil_div(a, b):
        if a % b == 0:
            return a / b
        else:
            return a // b + 1

    # A.sort()  # can this bring an improvement?

    # The average is the target value that each element should have, because it will, in average, require the least steps for all the elements.
    # It could be 2, since the average of [1..4] is 2, but each array could be different.
    avg = ceil_div(sum(A), len(A))
    steps = 0

    for i, val in enumerate(A):
        diff = avg - val
        steps += abs(diff)

    return steps


try:
    tests = [
        ([3, 2, 1, 1, 2, 3, 1], 5),
    ]

    for (test, expected) in tests:
        r = solution(test)
        print(r)
        assert r == expected

except AssertionError as e:
    print("assrtion error")
