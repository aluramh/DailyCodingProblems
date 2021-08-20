# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

from typing import List


def find_first_index_gt_or_equal_to_target(nums: List[int], target: int):
    """
    Finds the first index where there is a value that is greater than or equal
    to the target

    Runtime complexity: O(lg n)
    Input:
        - nums: int[]
        - target: int
    Output: int
    """
    def find(nums: int, low: int, high: int, target: int):
        nonlocal first_pos

        mid_index = low + (high - low) // 2
        mid = nums[mid_index]

        log_array = nums[low:high + 1]
        print(log_array)

        # Escape conditional of recursiveness
        if low > high:
            return

        if mid >= target:
            first_pos = mid_index
            return find(nums, low, mid_index - 1, target)

        # We don't care about going right...
        elif mid < target:
            return find(nums, mid_index + 1, high, target)

    first_pos = -1
    find(nums, 0, len(nums) - 1, target)
    return first_pos


def solve(nums: List[int], target: int):
    """
    Given an array of integers nums sorted in ascending order, finds the
    starting and ending position of a given target value.

    Input:
        - nums: int[]
        - target: int
    Output: (int, int)
    """
    if len(nums) == 0:
        return (-1, -1)

    # Find the first position "greater than, or equal to x
    first_pos = find_first_index_gt_or_equal_to_target(nums, target)

    # Find the first position "greater than, or equal to (x+1)". We do this
    # because if we find this, then if we go "-1" back the found index, we
    # will find the last ocurrence of x in the nums array
    end_pos = find_first_index_gt_or_equal_to_target(nums, target + 1) - 1

    # "first_pos" always has to be less or equal to the "end_pos" in a 
    # correct answer
    if first_pos <= end_pos:
        return (first_pos, end_pos)

    # else, check if we at least found a first appearance of the target
    elif nums[first_pos] == target:
        return (first_pos, first_pos)

    # else it was not found
    return (-1, -1)


try:
    # MARK: - Sample cases

    assert solve([5, 7, 7, 8, 8, 10], 6) == (-1, -1)
    assert solve([5, 7, 7, 8, 8, 10], 8) == (3, 4)

    # MARK: - Edge cases

    assert solve([1], 1) == (0, 0)
    assert solve([2], 1) == (-1, -1)
    assert solve([1], 2) == (-1, -1)
    assert solve([], 1) == (-1, -1)

    print('Success!')

except AssertionError as err:
    print(err)
