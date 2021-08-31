class Solution(object):
    def find_first_index_gt_or_equal_to_target(self, nums, target):
        def find(nums, low, high, target):
            nonlocal first_pos

            # Choose a "middle" (Only int values)
            mid_index = low + (high - low) // 2
            mid = nums[mid_index]

            # If the start is grater than the end, then the array empty, so just return
            if low > high:
                return

            # If the middle is equal to the target, we have to scan the left and right.
            if mid >= target:
                # If the middle is the target, then update this info...
                first_pos = mid_index
                # ...but keep looking on the left...
                return find(nums, low, mid_index - 1, target)

            # If the middle is less than the target, then scan the right
            elif mid < target:
                return find(nums, mid_index + 1, high, target)

        first_pos = -1
        # At the end of this main function, the value of [first] will have the 1st appearance of the target number.
        find(nums, 0, len(nums) - 1, target)
        return first_pos

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Find the first position "greater than, or equal to x
        first_pos = self.find_first_index_gt_or_equal_to_target(nums, target)

        # Find the first position "greater than, or equal to (x+1)". We do this
        # because if we find this, then if we go "-1" back the found index, we
        # will find the last ocurrence of x in the nums array
        end_pos = self.find_first_index_gt_or_equal_to_target(
            nums, target + 1) - 1

        # "first_pos" always has to be less or equal to the "end_pos" in a
        # correct answer
        if first_pos <= end_pos:
            return (first_pos, end_pos)

        elif end_pos == -2:
            if first_pos == -1:
            else:
            return (first_pos, len(nums) - 1)

        # else, check if we at least found a first appearance of the target
        elif nums[first_pos] == target:
            return (first_pos, first_pos)

        # else it was not found
        return (-1, -1)


sol = Solution()
r = sol.searchRange([2, 2], 3)
print(r)
