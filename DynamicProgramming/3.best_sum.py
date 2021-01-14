def best_sum_recursive(target_sum, numbers):
    if target_sum == 0: return []
    if target_sum < 0: return None

    # Is independant for each loop. Is not shared between recursions.
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


def best_sum(target_sum, numbers, memo):
    if target_sum in dict.keys(memo): return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    # Each recursion as its own shortest_combination
    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers, memo)

        if remainder_combination is not None:
            combination = remainder_combination + [num]

            if (shortest_combination is None) or (len(combination) <
                                                  len(shortest_combination)):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination


if __name__ == "__main__":
    try:
        print(best_sum(7, [5, 3, 4, 7], {}))
        assert best_sum(7, [5, 3, 4, 7], {}) == [7]

        print(best_sum(8, [2, 3, 5], {}))
        assert best_sum(8, [2, 3, 5], {}) == [5, 3]

        print(best_sum(7, [5, 3, 6], {}))
        assert best_sum(7, [5, 3, 6], {}) is None

        result = best_sum(8, [2, 3, 5], {})
        print(result)
        assert result == [5, 3]

        result = best_sum(100, [1, 2, 5, 25], {})
        print(result)
        assert result == [25, 25, 25, 25]

        result = best_sum(300, [7, 14], {})
        print(result)
        assert result is None

        print("Program finished with no errors 😉")

    except AssertionError as e:
        print(e)
        print("There was an assertion error")
