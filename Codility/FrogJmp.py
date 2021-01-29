# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    def ceildiv(a, b):
        return -(-a // b)

    memo = {}
    step_count = 0

    r = ceildiv((Y - X), D)

    return r


if __name__ == "__main__":
    try:
        tests = [
            ((10, 85, 30), 3),
            ((3, 999111321, 7), 142730189),
        ]

        for ((X, Y, D), expected_result) in tests:
            result = solution(X, Y, D)
            print(result)
            assert expected_result == result

    except AssertionError as e:
        print("Assertion error")
        print(e)
