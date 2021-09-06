from typing import List


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")


class Solution:
    def removeIslands(self, grid: List[List[str]]) -> int:
        """
        Given any grid of 1's and 0's, an island is a "1" that is not connected to the border by a path (up,down,left,right) of 1s.
        This function removes all the 1's that are not connected to the border.
        """

        # This will work like a "visited" matrix
        lands = {}
        count = 0

        def is_inside_bounds(x, y):
            firstRow = grid[0]
            is_inside = x >= 0 and y >= 0 and x < len(grid) and y < len(
                firstRow)
            return is_inside

        def is_border(x, y):
            firstRow = grid[0]

            is_top_or_bottom = x == 0 or x == len(grid) - 1
            is_left_or_right = y == 0 or y == len(firstRow) - 1

            return is_top_or_bottom or is_left_or_right

        def findLand(lands, x, y):
            # Recursively traverse the neighbors until there are no more neighbors to traverse.
            # Mark them as visited and return 1 when finished.
            steps = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
            ]

            for dx, dy in steps:
                new_x = x + dx
                new_y = y + dy
                # Add dash to make them even more unique keys without collisions if grid gets too big
                key = f"{new_x}-{new_y}"

                if is_inside_bounds(new_x, new_y) and grid[new_x][new_y] == "1":
                    if key not in lands:
                        # mark as visited so we don't do it in the future
                        lands[key] = True
                        # Recursively traverse the neighbors of the neighbors. This is DFS.
                        # O(n) = O(n+m)
                        findLand(lands, new_x, new_y)

            return 1

        # Loop through all the grid items
        for i, row in enumerate(grid):
            # Only the last items from the row
            for j, col in enumerate(row):
                if grid[i][j] == "1" and is_border(i, j):
                    key = f"{i}-{j}"

                    if key not in lands:
                        found_land = findLand(lands, i, j)
                        count += found_land

        # Loop again to remove the 1's that are not in the land
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                key = f"{i}-{j}"

                if grid[i][j] == "1" and key not in lands:
                    # Set a val of "0" to remove it
                    grid[i][j] = "0"

        # print(lands)
        print_grid(grid)
        return count


tests = [
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ],
    [
        [
            "1", "0", "0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0",
            "0", "0", "0", "0", "0", "0", "0"
        ],
        [
            "1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0",
            "1", "0", "1", "0", "0", "1", "0"
        ],
        [
            "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0",
            "0", "0", "0", "1", "0", "1", "0"
        ],
        [
            "0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "1",
            "1", "0", "0", "1", "0", "0", "1"
        ],
        [
            "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0",
            "0", "0", "0", "0", "0", "0", "0"
        ],
        [
            "1", "0", "0", "0", "0", "1", "0", "1", "0", "1", "1", "0", "0",
            "0", "0", "0", "0", "1", "0", "1"
        ],
        [
            "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0",
            "1", "0", "1", "0", "1", "0", "1"
        ],
        [
            "0", "0", "0", "1", "0", "1", "0", "0", "1", "1", "0", "1", "0",
            "1", "1", "0", "1", "1", "1", "0"
        ],
        [
            "0", "0", "0", "0", "1", "0", "0", "1", "1", "0", "0", "0", "0",
            "1", "0", "0", "0", "1", "0", "1"
        ],
        [
            "0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "0", "1", "0",
            "0", "1", "0", "0", "0", "1", "0"
        ],
        [
            "1", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0",
            "0", "1", "0", "1", "0", "1", "0"
        ],
        [
            "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "1", "0", "1",
            "1", "1", "0", "1", "1", "0", "0"
        ],
        [
            "1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "0",
            "0", "0", "1", "0", "0", "0", "1"
        ],
        [
            "0", "1", "0", "0", "1", "1", "1", "0", "0", "0", "1", "1", "1",
            "1", "1", "0", "1", "0", "0", "0"
        ],
        [
            "0", "0", "1", "1", "1", "0", "0", "0", "1", "1", "0", "0", "0",
            "1", "0", "1", "0", "0", "0", "0"
        ],
        [
            "1", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0",
            "0", "1", "0", "1", "0", "1", "1"
        ],
        [
            "1", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0",
            "1", "0", "1", "0", "0", "0", "0"
        ],
        [
            "0", "1", "1", "0", "0", "0", "1", "1", "1", "0", "1", "0", "1",
            "0", "1", "1", "1", "1", "0", "0"
        ],
        [
            "0", "1", "0", "0", "0", "0", "1", "1", "0", "0", "1", "0", "1",
            "0", "0", "1", "0", "0", "1", "1"
        ],
        [
            "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0",
            "0", "0", "1", "1", "0", "0", "0"
        ],
    ],
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "1", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ],
]

try:
    for grid in tests:
        r = Solution().removeIslands(grid)

except AssertionError:
    print("Error!")
