import numpy as np


def fibonacci_recursive(n):
    def fib(n):
        if n <= 2:
            return 1

        else:
            val = fib(n - 1) + fib(n - 2)
            return val

    return fib(n)


def fibonacci_dynamic(n):
    dict = {}

    for x in range(0, n + 1):
        if x <= 2:
            dict[x] = 1
        else:
            dict[x] = dict[x - 2] + dict[x - 1]

    return dict[n]


def fib_tabulation(n):
    table = np.zeros(n + 1, dtype=int)
    table[0] = 0
    table[1] = 1

    for (i, x) in enumerate(table):
        if i + 1 < len(table):
            table[i + 1] += table[i]

        if i + 2 < len(table):
            table[i + 2] += table[i]

    return table[n]


print(fibonacci_recursive(8))
print(fibonacci_dynamic(8))
print(fib_tabulation(8))
