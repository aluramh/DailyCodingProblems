# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time
# and constant space. In other words, find the lowest positive integer that does
# not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

INF = 99999999999


# O(n lg n)
def other_solution(numbers):
    # Sort
    # O(n lg n)
    numbers.sort()

    # Remove duplicates
    # O(n)
    filtered_iterable = list(filter(lambda x: x > 0, numbers))

    # Iterate and find the first false index==number
    # O(n)
    for index, number in enumerate(filtered_iterable, start=1):
        if index != number:
            return index

    return index + 1


def solution(numbers):
    lowest = INF
    largest = -INF

    for number in numbers:
        # Discard negatives
        if number < 0:
            break

        # Update min
        if number < lowest:
            lowest = number

        # Update max
        if number > largest:
            largest = largest

    # decide on min or max
    # result =

    print(lowest)
    return lowest


def set_solution(numbers):
    # Build set
    # Each insertion in a set is O(1), thus:
    # O(n)
    set_numbers = set(numbers)

    # Iterate and find the first false index that is not inside the set
    # O(n)
    index = 1
    while index in set_numbers:
        index += 1

    return index


try:
    assert other_solution([3, 4, -1, 1]) == 2
    assert set_solution([3, 4, -1, 1]) == 2
    print('Passed test 1')

    assert other_solution([1, 2, 0]) == 3
    assert set_solution([1, 2, 0]) == 3
    print('Passed test 2')

except AssertionError as error:
    print('FAILED')