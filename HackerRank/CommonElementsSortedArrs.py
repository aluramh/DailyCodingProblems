from typing import List


def binary_search(arr: List[int], x: int) -> int:
    """ 
    Input:
        arr: list of ints
        x: int to look for
    Output:
        int of index of val in arr
    """
    def helper(low, high):
        if high >= low:
            middle = (high + low) // 2

            if arr[middle] == x:
                return middle

            # Our element is to the right of the middle
            elif x > arr[middle]:
                return helper(middle + 1, high)

            # Out element is to the left of the middle
            elif x < arr[middle]:
                return helper(low, middle - 1)
        else:
            return -1

    return helper(0, len(arr) - 1)


# tests = [
#     # ([1, 2, 3, 4], 3),
#     # ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
#     ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11),
# ]

# for arr, x in tests:
#     r = binary_search(arr, x)
#     res = arr[r]
#     print(r)
#     assert x == res


def common_elements(m: List[int], n: List[int]) -> List[int]:
    """
    Input:
        m: Distinct and Sorted array of ints
        n: Distinct and Sorted array of ints
    Output:
        common: Common elements between the 2 arrays
    """
    def iterative_helper(m, n):
        j = 0
        i = 0
        common = []

        while (i < len(n) - 1) or (j < len(m) - 1):
            x = n[i]
            y = m[j]

            if x == y:
                common.append(x)
                j += 1
                i += 1
            elif x < y:
                while x < y and (i < len(n) - 1):
                    i += 1
                    x = n[i]
            elif x > y:
                while x > y and (j < len(m) - 1):
                    j += 1
                    y = m[j]

        return common

    def binary_search_helper(m, n):
        """
        perform binary search in "n".
        n should be bigger than m.
        """
        big = m
        small = n

        common = []
        for x in big:
            r = binary_search(small, x)
            if r != -1:
                common.append(x)

        return common

    return binary_search_helper(m, n)


tests = [
    ([1, 5, 15, 20], [2, 5, 13, 30], [5]),
    ([1, 5, 15, 20, 30, 37], [2, 5, 13, 30, 32, 35, 37, 42], [5, 30, 37]),
]

for m, n, expected_result in tests:
    r = common_elements(m, n)
    print(r)
    assert r == expected_result
