from typing import List


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
