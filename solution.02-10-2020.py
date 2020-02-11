# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the
# first and last element of that pair. For example, car(cons(3, 4)) returns 3,
# and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:


# Anything built with "cons" outputs a function that uses a,b as input params
def cons(a, b):
    # Define a function that takes a function and sends (a,b)
    def pair(f):
        return f(a, b)

    # Return that function definition
    return pair


def car(pair):
    # Pair is an anonymous function THAT TAKES an anonymous function that uses (a,b)
    def return_first(*tuple_item):
        return tuple_item[0]

    return pair(return_first)


def cdr(pair):
    return pair(lambda a, b: b)


# Implement car and cdr.
result1 = car(cons(3, 4))  # returns 3
print(result1)

result2 = cdr(cons(3, 4))  # returns 4
print(result2)