# Given a 2D matrix matrix, handle multiple queries of the following type:
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Approach 2 Time O(1) SPace O(mn)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])

        self.dp = [[0 for j in range(n+1)] for i in range(m + 1)]
        if m == 0 or n == 0:
            return 
        for r in range(m):
            for c in range(n):
                self.dp[r+1][c+1] = self.dp[r+1][c]+ self.dp[r][c+1] + matrix[r][c] - self.dp[r][c]
        # print(self.dp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2+1]- self.dp[row1][col2 +1] - self.dp[row2+1][col1]+ self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



# Approach 1
# TIme complexity: O(m) => m = no. of rows
import numpy
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0 for j in range(n+1)] for i in range(m)]
        if m == 0 or n == 0:
            return 
        for r in range(m):
            for c in range(n):
                self.dp[r][c+1] = self.dp[r][c] + matrix[r][c]
        # print(self.dp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sm = 0
        for r in range(row1, row2+1):
            sm += self.dp[r][col2+1] - self.dp[r][col1]
        return sm


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

