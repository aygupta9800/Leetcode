class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix), len(matrix[0])
        self.dp = [[matrix[i][j] for j in range(n)] for i in range(m)]
        for i in range(1,n):
            self.dp[0][i] += self.dp[0][i-1]
        for j in range(1,m):
            self.dp[j][0] += self.dp[j-1][0]
        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] += self.dp[i-1][j]+ self.dp[i][j-1]-self.dp[i-1][j-1]
        print(self.dp)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        if col1 !=0:
            ans += self.dp[row2][col1 -1]
        if row1 !=0:
            ans += self.dp[row1-1][col2]
        if row1 !=0 and col1 != 0:
            ans -= self.dp[row1-1][col1-1]
        return self.dp[row2][col2] -ans
            
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)