from typing import List, Tuple

memo = {}


def helper(
    list: List[Tuple[int, int]],
    S: int,
    i: int,
    selected: List[Tuple[int, int]],
):
    if i >= len(list):
        return selected, 0

    weight, val = list[i]

    with_item_val = 0
    if weight <= S:
        helper_val = helper(list, S - weight, i + 1, selected + [list[i]])
        with_item_val = val + helper_val[1]

    without = helper(list, S, i + 1, selected)

    if with_item_val > without[1]:
        return helper_val[0], with_item_val
    else:
        return without


def knapsack(list, S):
    return helper(list, S, 0, [])


# (weight, value)
tests = [
    ([(4, 5)], 6),
    ([(4, 5), (5, 10), (2, 6)], 6),
    ([(1, 4), (4, 6), (10, 2), (5, 5)], 10),
    ([(5, 1), (14, 6), (0, 21), (6, 9), (9, 9), (3, 2), (1, 1), (0, 0)], 4),
]

for (items, S) in tests:
    r = knapsack(items, S)
    print(r)
