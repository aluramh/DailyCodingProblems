# Problem #1

# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


# Runtime: O(n)
# Space: O(2n)
def main(number_list, target):
    past_numbers = {}

    for number in number_list:
        # Number we need
        look_for = target - number
        # Check if number we need is in the dictionary
        needed_number = past_numbers.get(look_for, None)
        if needed_number is not None:
            # If it is, return true
            return True

        # Else, add it to a list of previously found numbers
        past_numbers[number] = number

    # If the loop has ended and "True" was not returned, return false
    return False


INPUT = [10, 15, 3, 7]
K = 17
result = main(INPUT, K)
print(result)