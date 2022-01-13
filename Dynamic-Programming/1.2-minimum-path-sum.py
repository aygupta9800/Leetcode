#Approach3 without extra space
# TIme O(m.n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        if we know distance of point from end, and overwrite the original grid
        then grid[r][c] = grid(r,c)+ min(grid[r+1][c], gridr][c+1])
        """
        m, n = len(grid), len(grid[0])
        # dp = [0 for i in range(n)]
        # print(dp)
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c != n-1:
                    grid[r][c] = grid[r][c] + grid[r][c+1]
                elif c == n-1 and r != m-1:
                    grid[r][c] = grid[r][c] + grid[r+1][c]
                elif r != m-1 and c != n-1:
                    grid[r][c] = grid[r][c] + min(grid[r+1][c],grid[r][c+1])
                # else: # last elem of grid
                #     dp[c = grid[r][c]
                    
        return grid[0][0]
#Approach2 USing 1D Array
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        we just need bottom and right elem value to find min sum for a point
        bottom sum is already there in single array
        """
        m, n = len(grid), len(grid[0])
        dp = [0 for i in range(n)]
        # print(dp)
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c != n-1:
                    dp[c] = grid[r][c] + dp[c+1]
                elif c == n-1 and r != m-1:
                    dp[c] = grid[r][c] + dp[c]
                elif r != m-1 and c != n-1:
                    dp[c] = grid[r][c] + min(dp[c],dp[c+1])
                else: # last elem of grid
                    dp[c] = grid[r][c]
                    
        return dp[0]

#Approach 1 Using DP 2D
# Time complexity : O(mn)O(mn). We traverse the entire matrix once.

# Space complexity : O(mn)O(mn). Another matrix of the same size is used.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        if we know distance of point from end
        then dp[r][c] = min(dp[r+1][c], dp[r][c+1])
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        # print(dp)
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c != n-1:
                    dp[r][c] = grid[r][c] +dp [r][c+1]
                elif c == n-1 and r != m-1:
                    # print(r, c)
                    dp[r][c] = grid[r][c] + dp[r+1][c]
                elif r != m-1 and c != n-1:
                    dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
                else: # last elem of grid
                    dp[r][c] = grid[r][c]
                    
        return dp[0][0]