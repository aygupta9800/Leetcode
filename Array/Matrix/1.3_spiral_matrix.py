# Given an m x n matrix, return all elements of the matrix in spiral order.

# Approach 1 Setting boundaries O(m*n) time , O(1) space
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, cols = len(matrix), len(matrix[0])
        left, top = 0, 0
        right, bottom = cols -1, rows -1
        
        while top <= bottom and left <= right:
            # Traverse from left to right.
            for col in range(left, right+1):
                result.append(matrix[top][col])
            top += 1
            # Traverse downwards.
            for row in range(top, bottom +1):
                result.append(matrix[row][right])
            right -= 1
             # Make sure we are now on a different row.
            if top <= bottom:
                # Traverse from right to left.
                for col in range(right, left -1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            # Make sure we are now on a different column.
            if left <= right:
                # Traverse upwards.
                for row in range(bottom, top -1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result