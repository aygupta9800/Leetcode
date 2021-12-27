# Approach 4: Search Space Reduction 
# Time O(m + n) spaceO(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) ==0:
            return False
        
        m,n = len(matrix), len(matrix[0])
        
        row, col = m-1, 0
        
        while col <n and row>=0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False