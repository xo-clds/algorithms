# Unique Paths

from functools import lru_cache as cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of unique paths to each cell
        # dp = [[1] * n for _ in range(m)]

        # # Fill the dp array
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # # The bottom-right cell contains the number of unique paths
        # return dp[m - 1][n - 1]

        # Time complexity: O(m * n)
        # Space complexity: O(m * n)

        # Using combinatorial approach

        return self.factorial(m + n - 2) // (self.factorial(m - 1) * self.factorial(n - 1))
        # Time complexity: O(m + n)
        # Space complexity: O(m + n)

    @cache(maxsize=128, typed=True)  # noqa: B019
    def factorial(self, x: int) -> int:
        if x in {0, 1}:
            return 1

        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
