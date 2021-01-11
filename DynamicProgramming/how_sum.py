# https://youtu.be/oBt53YbR9Kk?t=5370

# Input:
#   - target_sum
#   - array of numbers

# Output:
#   - Array that adds up to target_sum OR null if not possible

# NOTE: - If multiple combinations, return a single one


def how_sum_recursive(target_sum, numbers):
    def helper(target_sum):
        # We return an empty array because by "not choosing a number" we can always "add up" to 0
        if target_sum == 0:
            return []
        # Only positive numbers are valid, so we cannot "add up" to negative numbers
        if target_sum < 0:
            return None

        for num in numbers:
            # Get back the array of the recursive call that adds up to target_sum
            result = helper(target_sum - num)

            # If the result is not none, it is a valid array, so return it and end the loop
            if result is not None:
                # Return the array of the result + the number
                return [num] + result

        # We looped through everything and there is no value. Return.
        return None

    return helper(target_sum)


def how_sum(target_sum, numbers):
    store = {}

    def helper(target_sum):
        # If the result has already been memoized, then just return it
        if target_sum in dict.keys(store):
            return store[target_sum]

        # NOTE: - DO NOT MEMOIZE. PREMATURE MEMOIZATION. For these base cases return the value itself.
        #         That will be done automagically further down the recursion.

        # We return an empty array because by "not choosing a number" we can always "add up" to 0
        if target_sum == 0:
            return []
        # Only positive numbers are valid, so we cannot "add up" to negative numbers
        if target_sum < 0:
            return None

        for num in numbers:
            # Get back the array of the recursive call that adds up to target_sum
            result = helper(target_sum - num)

            # If the result is not none, it is a valid array, so return it and end the loop
            if result is not None:
                # Return the array of the result + the number
                store[target_sum] = [num] + result
                return store[target_sum]

        # We looped through everything and there is no value. Return.
        store[target_sum] = None
        return None

    return helper(target_sum)


if __name__ == "__main__":
    try:
        # ANCHOR: - Recursion

        result = how_sum_recursive(7, [5, 3, 4, 7])
        assert isinstance(result, list) is True

        result = how_sum_recursive(7, [5, 3, 6])
        assert isinstance(result, list) is False

        # Deep recursion problem => Stack overflow
        # result = how_sum_recursive(300, [7, 14])
        # assert (isinstance(result, list) is None)

        # ANCHOR: - Dynamic programming

        result = how_sum(7, [5, 3, 4, 7])
        print(result)
        assert isinstance(result, list) is True

        result = how_sum(7, [5, 3, 6])
        print(result)
        assert isinstance(result, list) is False

        result = how_sum(8, [2, 3, 5])
        print(result)

        result = how_sum(300, [7, 14])
        print(result)
        assert isinstance(result, list) is False

        print("Program finished with no errors 😉")

    except AssertionError as e:
        print(e)
        print("There was an assertion error")
