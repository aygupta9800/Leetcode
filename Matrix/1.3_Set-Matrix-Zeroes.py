class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colZero = False
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    if c == 0:
                        colZero = True
                    else:
                        matrix[0][c] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0
        
        if colZero:
            for r in range(m):
                matrix[r][0] = 0
               
                    
       
        
        