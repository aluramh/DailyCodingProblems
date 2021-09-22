from typing import List


class Solution:
    ans = []

    def intervalIntersection(
        self,
        firstList: List[List[int]],
        secondList: List[List[int]],
    ) -> List[List[int]]:
        return self.helper(firstList, secondList, 0, 0, [])

    def helper(self, A, B, i, j, ans):
        # If either i or j is greater than their array, then there will be no
        # more intersections, so we can end here
        if i >= len(A) or j >= len(B):
            return ans

        # Let's check if A[i] intersects B[j].
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection
        low = max(A[i][0], B[j][0])
        high = min(A[i][1], B[j][1])
        if low <= high:
            ans.append([low, high])

        # Remove the interval with the smallest endpoint
        if A[i][1] < B[j][1]:
            return self.helper(A, B, i + 1, j, ans)
        else:
            return self.helper(A, B, i, j + 1, ans)


tests = [
    (
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]],
    ),
]

for t in tests:
    r = Solution().intervalIntersection(t[0], t[1])
    print(r)
