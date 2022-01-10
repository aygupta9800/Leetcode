# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n -1
        while left <= right:
            mid = (left+right) //2
            # IMP POINT
            r, c = mid // n, mid % n
            
            if matrix[r][c] == target:
                return True
            if target < matrix[r][c]:
                right= mid -1
            else:
                left = mid + 1
        return False
            