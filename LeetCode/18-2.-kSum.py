from typing import List


class SolutionDefault:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            # Check if the sum of k smallest values is greater than target
            check_smallest = (nums[0] * k > target)

            # Check if the sum of k largest values is smaller than target.
            check_largest = (target > nums[-1] * k)

            if len(nums) == 0 or check_smallest or check_largest:
                return res

            # When we are down to 2, then we use the twoSum algorithm
            if k == 2:
                return twoSum(nums, target)

            # Loop i through the whole array of nums
            for i in range(len(nums)):
                # If the value is the same as the one before it, skip it
                # (we would be adding duplicates to the answer).
                # Also, do not do this check for the first value of the array,
                # otherwise it would be the last item...
                if i == 0 or nums[i - 1] != nums[i]:
                    # Generate all the subsets for the rest of the array
                    # excluding the pos "i".

                    # To do this, the new subarray we will focus on is one
                    # that excludes the current [i] index
                    subarray = nums[i + 1:]

                    # Since we want to get all the possible k-1 sums of the
                    # remaining of the array, given this [i]
                    # the target also has to change to a value diff. value of
                    # the current target - the current nums[i]
                    new_target = target - nums[i]

                    # Finally, since we're going 1 level deeper, we need to
                    # decrease the [k] value
                    new_k_sum = k - 1

                    # With all of these new parameters, recursively calculate
                    # the subset of possible answers that match the target
                    # when adding nums[i]
                    subsets = kSum(subarray, new_target, new_k_sum)
                    # all of the subsets available are part of a solution when
                    # appended with [nums[i]]
                    for subset in subsets:
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()

            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])

            return res

        nums.sort()
        return kSum(nums, target, 4)


class Solution:
    def isOriginal(self, sols, incoming):
        for sol in sols:
            if sorted(sol) == sorted(incoming):
                return False
        return True

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort!
        # nums = sorted(nums) # assume sorted

        threes = []
        i = 0

        while i + 1 < len(nums) - 1:  # because it's in threes
            low = i + 1
            high = len(nums) - 1

            # 2Sum problem
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]

                if three_sum == target:
                    sol = [nums[low], nums[i], nums[high]]
                    if sol not in threes:
                        threes.append(sol)
                    low += 1

                elif three_sum < target:
                    low += 1

                elif three_sum > target:
                    high -= 1

            # Close off the set from the left side
            i += 1

        # We have already gone through all the array, so just exit the
        return threes

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        i = 0
        while i < len(nums):
            new_target = target - nums[i]

            three_sums = self.threeSum(nums[i + 1:], new_target)

            for sol in three_sums:
                possible = [nums[i]] + sol

                if self.isOriginal(res, possible) is True:
                    res.append(possible)

            i += 1

        return res


tests = [
    ([1, 0, -1, 0, -2, 2], 0),
]

r = SolutionDefault().fourSum([1, 0, -1, 0, -2, 2], 0)
print(r)
