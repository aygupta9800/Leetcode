# https://leetcode.com/problems/unique-paths/

# There is a robot on an m x n grid. The robot is initially located at the top-left
# corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
#  The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] *m
        # print(dp)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] +dp[i][j+1]
        return dp[0][0]