arr_subset = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]


def hourglassSum(arr):
    def convert_to_matrix(arr):
        lines = arr.split('\n')
        matrix = list(
            map(lambda line: list(map(lambda x: int(x), line.split())), lines))
        return list(matrix)

    m = convert_to_matrix(arr)

    # We'll use i and j to traverse and it will limit our values so we don't
    # grab an out of bounds item

    memo = {}
    max_sum = None
    j = 0
    for i in range(4):
        for j in range(4):
            hourglass_sum = m[i][j] + m[i][j + 1] + m[i][j + 2]
            hourglass_sum += m[i + 1][j + 1]
            hourglass_sum += m[i + 2][j] + m[i + 2][j + 1] + m[i + 2][j + 2]

            if max_sum is None or max_sum < hourglass_sum:
                max_sum = hourglass_sum

            key = f"{i}{j}"
            memo[key] = hourglass_sum
            if key == "12":
                print()

    return max_sum


tests = [
    ("""1 1 1 0 0 0
        0 1 0 0 0 0
        1 1 1 0 0 0
        0 0 2 4 4 0
        0 0 0 2 0 0
        0 0 1 2 4 0""", 19),
    ("""0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0""", 0),
    ("""0 0 0 0 0 0
        0 0 0 1 0 0
        0 0 0 0 0 0
        1 0 0 0 0 0
        0 -2 0 0 0 0
        0 0 0 0 0 0""", 1),
]

for arr, expected_result in tests:
    r = hourglassSum(arr)
    print(r)
    assert r == expected_result
