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


print(fibonacci_recursive(8))
print(fibonacci_dynamic(8))
