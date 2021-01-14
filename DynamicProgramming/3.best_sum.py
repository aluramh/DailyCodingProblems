def best_sum_recursive(target_sum, numbers):
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum_recursive(remainder, numbers)

        if remainder_combination is not None:
            combination = remainder_combination + [num]

            if (shortest_combination is None) or (len(combination) <
                                                  len(shortest_combination)):
                shortest_combination = combination

    return shortest_combination


def best_sum(target_sum, numbers, memo={}):
    if target_sum in dict.keys(memo): return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers)

        if remainder_combination is not None:
            combination = remainder_combination + [num]

            if (shortest_combination is None) or (len(combination) <
                                                  len(shortest_combination)):
                shortest_combination = combination

    return shortest_combination


if __name__ == "__main__":
    try:
        # ANCHOR: - Recursion

        result = best_sum_recursive(7, [5, 3, 4, 7])
        print(result)
        assert isinstance(result, list) is True

        result = best_sum_recursive(7, [5, 3, 6])
        print(result)
        assert isinstance(result, list) is False

        # Deep recursion problem => Stack overflow
        # result = how_sum_recursive(300, [7, 14])
        # assert (isinstance(result, list) is None)

        # ANCHOR: - Dynamic programming

        # result = best_sum(7, [5, 3, 4, 7])
        # print(result)
        # assert isinstance(result, list) is True

        # result = best_sum(7, [5, 3, 6])
        # print(result)
        # assert isinstance(result, list) is False

        # result = best_sum(8, [2, 3, 5])
        # print(result)

        # result = best_sum(300, [7, 14])
        # print(result)
        # assert isinstance(result, list) is False

        print("Program finished with no errors 😉")

    except AssertionError as e:
        print(e)
        print("There was an assertion error")
