from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # NOTE: PIVOT IS NOT GUARANTEED
        visited_middles = {}

        def findPivotIndex(nums, low, high):
            """
            Uses binary search but for finding a pivot.
            Because there are duplicates, we may be searching in the middle more than 1, so keep track of nodes we've visited
            """
            nonlocal visited_middles

            if high < low:
                return None

            m = low + (high - low) // 2

            # check if we've already visited this index as the mid
            if visited_middles.get(m):
                # Return None, as this has already been computed
                return None
            else:
                # Mark this middle has visited. In the future we will get receive answer
                visited_middles[m] = True

                # the pivot is when the item to the right of the mid is less than the mid
                if nums[m] > nums[m + 1]:
                    return m + 1

                # For these next, we need to include the middle as a value!
                # pivot is to the right
                # elif nums[m] > nums[high]:
                l_p = findPivotIndex(nums, m, high)
                if l_p is not None:
                    return l_p

                # pivot is to the left
                # elif nums[m] < nums[low]:
                r_p = findPivotIndex(nums, low, m)
                if r_p is not None:
                    return r_p

        # ANCHOR: - Main logic

        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]

        first = nums[0]
        last = nums[len(nums) - 1]

        # array was rotated enough times to be in order again.
        if first < last:
            return nums[0]
        else:
            # perform modified binary search to find pivot
            pivot_index = findPivotIndex(nums, 0, len(nums) - 1)

            # If no pivot was found, then return the first item from the array
            if pivot_index is None:
                return first
            else:
                return nums[pivot_index]


try:
    tests = [
        ([10, 1, 10, 10, 10, 10, 10], 1),
        ([1], 1),
        ([], None),
        ([10, 1], 1),
        ([10, 11, 12, 134, 0, 3, 5], 0),
    ]

    for (nums, expected_result) in tests:
        result = Solution().findMin(nums)
        print(result)
        assert result == expected_result

except AssertionError as e:
    print("Assertion error")
