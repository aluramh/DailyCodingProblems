class Solution:
    # O(n^2) - space O(1)
    def twoSumQuadratic(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]

                j += 1
            i += 1

    # O(2n) - space O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through the array and get the memo of all possibilities
        memo = {}

        for i, n in enumerate(nums):
            memo[n] = i
        print(memo)

        # Loop again until you find a target
        for i, n in enumerate(nums):
            looking_for = target - n
            # key = f"{looking_for}"
            print("Looking for", looking_for)

            if looking_for in memo:
                j = memo.get(looking_for)
                # Check that they are not the same item
                if i != j:
                    return [i, j]
