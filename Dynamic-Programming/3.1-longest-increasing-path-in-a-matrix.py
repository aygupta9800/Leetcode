# Time complexity O(m*n) space O(m*n)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # we will use a cache top down approach
        dp = [[-1] * n for i in range(m)]
        
        def dfs(r, c, prevVal):
            if r < 0 or r >= m or c < 0 or c >=n or matrix[r][c] <= prevVal:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            # we dont need to check if the maxm path is using prev value as it will contradict with our first check and return 0 before.
            # res = 1
            # res = max(res, 1+dfs(r+1, c, matrix[r][c]))
            # res = max(res, 1+dfs(r-1, c, matrix[r][c]))
            # res = max(res, 1+dfs(r, c+1, matrix[r][c]))
            # res = max(res, 1+dfs(r, c-1, matrix[r][c]))
                   
            res = 1 + max(dfs(r+1, c, matrix[r][c]), dfs(r-1, c, matrix[r][c]),\
                          dfs(r, c+1, matrix[r][c]),dfs(r, c-1, matrix[r][c]))
            dp[r][c] = res
            return res
        
        for r in range(m):
            for c in range(n):
                dfs(r, c, -1)
        
        return max(dp[i][j] for i in range(m) for j in range(n))
        