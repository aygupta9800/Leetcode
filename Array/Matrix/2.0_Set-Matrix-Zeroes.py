class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        rowZero = False
        #determine which row/colms need to bezero
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r>0: 
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1,R):
            for c in range(1,C):
                if matrix[0][c] ==0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        for r in range(R):
            if matrix[0][0] == 0:
                matrix[r][0] = 0
        for c in range(C):
            if rowZero:
                matrix[0][c] = 0
        
                    
       
        
        