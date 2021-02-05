import numpy


def grid_traveler(m, n):
    matrix = numpy.zeros((m + 1, n + 1), dtype=int)

    matrix[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            current_element = matrix[i][j]

            # Add to down neighbor
            if i + 1 <= m:
                matrix[i + 1][j] += current_element

            # Add to right neighbor
            if j + 1 <= n:
                matrix[i][j + 1] += current_element

    return matrix[m][n]


res = [
    # (1, 1),
    (2, 3),
    (3, 2),
    (3, 3),
    (18, 18),
]

for m, n in res:
    r = grid_traveler(m, n)
    print(r)
