import numpy


def can_sum(target, A):
    matrix = numpy.zeros(target + 1, dtype=bool)
    matrix[0] = True

    for i in range(target + 1):
        current = matrix[i]

        if current == True:
            for num in A:
                if num + i < len(matrix):
                    matrix[num + i] = True

    return matrix[target]


def create_list(size, initial):
    l = []
    for i in range(size + 1):
        l.append(initial)
    return l


def how_sum(target, A):
    matrix = create_list(target + 1, None)
    matrix[0] = []

    for i in range(target + 1):
        current = matrix[i]

        if current is not None:
            for num in A:
                if num + i < len(matrix):
                    matrix[num + i] = current + [num]

    return matrix[target]


def best_sum(target, A):
    matrix = create_list(target + 1, None)
    matrix[0] = []

    for i in range(target + 1):
        current = matrix[i]

        if current is not None:
            for num in A:

                if num + i < len(matrix):
                    new_possible = current + [num]
                    current_possible = matrix[num + i]

                    # The way we decide which option we choose is we preferr the shortest
                    if (current_possible is None) or (len(new_possible) <
                                                      len(current_possible)):
                        matrix[num + i] = new_possible
                    # else:
                    #     # Do not change
                    #     # matrix[num + i] = matrix[num + i]
                    #     pass

    return matrix[target]


tests = [
    (7, [5, 3, 4]),
    (8, [2, 3, 5]),
    (100, [1, 2, 5, 25]),
    (199, [2, 5, 25, 99]),
]

for target, A in tests:
    print('Target:', target)

    r = can_sum(target, A)
    print('can_sum:', r)

    r = how_sum(target, A)
    print('how_sum:', r)

    r = best_sum(target, A)
    print('best_sum:', r)

    print()
