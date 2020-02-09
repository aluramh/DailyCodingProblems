# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the
# new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# e.g.
# 2 = 2 * 1
# 3 = 3 * 1
# 6 = 2 * 3
# A = [2, 3, 6]

# Follow-up: what if you can't use division?


# O(n)
def get_products(array, excluded_index):
    product = None
    for i in range(len(array)):
        # Only proceed with the calculation if the index is not excluded
        if i != excluded_index:
            # Initialize the product if needed
            if product == None:
                product = array[i]
            else:
                product = (product * array[i])

    return product


# Brute force solution:
# O(n^2)
def brute_force_solution(input):
    answer = []

    # O(n)
    for i in range(len(input)):
        # O(n)
        iteration_product = get_products(input, i)
        answer.append(iteration_product)

    return answer


# O(2n)
def solution_with_division(input):
    # Loop once and get an array of all the products
    total_product = None
    for i in range(len(input)):
        if total_product == None:
            total_product = input[i]
        else:
            total_product *= input[i]

    # Loop twice and get the division of input[i]
    result = []
    for i in range(len(input)):
        # TODO: - Handle case where divisor is 0
        divisor = input[i]
        result.append(int(total_product / divisor))

    return result


# Solution without division
def solution():
    print()


INPUT = [1, 2, 3, 4, 5]
result = solution_with_division(INPUT)
print('\n', result)
