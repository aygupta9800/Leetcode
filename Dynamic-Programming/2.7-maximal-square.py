# Approach 1 Using 2d array
# dp[i][j] = min(dp[i,j-1],dp[i-1, j],dp[i][j]) +1
# where dp[i][j] represents max len of square ending at i, j as right bottom corner
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        dp = [[0 for c in range(n)] for r in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] =  1 if matrix[r][c] == '1' else 0
                elif matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c])+1
                else:
                    dp[r][c] = 0
                ans = max(ans, dp[r][c])
                    
        return ans * ans


# Approach2 Using 1d array
# As we are only using prev row dp values + prev value 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        dp = [0 for c in range(n)]
        for r in range(m):
            prev = 0 # here prev represents prev col same row value
            for c in range(n):
                temp = dp[c] # we use temp to set prev value before updating current dp value
                if r == 0 or c == 0:
                    dp[c] =  1 if matrix[r][c] == '1' else 0
                elif matrix[r][c] == '1':
                    temp = dp[c]
                    dp[c] = min(dp[c], dp[c-1], prev)+1
                    
                else:
                    dp[c] = 0
                prev = temp
                ans = max(ans, dp[c])
        return ans * ans
        
        