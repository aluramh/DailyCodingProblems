# 1648. Sell Diminishing-Valued Colored Balls
# Medium

# Add to List

# Share
# You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

# The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

# You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

# Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

from typing import List
import heapq


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        total_profit = 0
        reverse_inventory = list(map(lambda x: -x, inventory))

        if len(inventory) == 1:
            # (10/2)(1 + 10)
            start = inventory[0] - orders
            end = inventory[0]

            result = (orders / 2) * ((start + 1) + end)
            return int(result)

        for order in range(1, orders + 1):
            heapq.heapify(reverse_inventory)

            # Get the max
            # O(n)
            min_in_inventory = reverse_inventory[0]
            # and add it as the earnings
            total_profit += min_in_inventory

            # Find the max in the array and decrease it by 1
            # O(1)
            reverse_inventory[0] += 1

        return -total_profit

    # def grab_max():
    #     pass


if __name__ == "__main__":
    try:
        tests = [
            # ([2, 5], 4, 14),
            # ([3, 5], 6, 19),
            # ([2, 8, 4, 10, 6], 20, 110),
            ([10], 5, 40),
            ([10], 10, 55),
            ([1000000000], 1000000000, 500000000500000000),
        ]

        # Sn = (n / 2)(u1 + un)
        # s10 =

        for (inventory, orders, expected_result) in tests:
            result = Solution().maxProfit(inventory, orders)
            print(result)
            assert result == expected_result

    except AssertionError as e:
        print("Assertion error")
        print(e)
