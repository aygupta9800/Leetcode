# Given an m x n matrix, return all elements of the matrix in spiral order.

# Approach 1 Setting boundaries O(m*n) time , O(1) space
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n-1
        top, bottom = 0, m -1
        
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
             # than the one which we used for left to right movement
            if top <= bottom:
                # Traverse from right to left.
                for col in range(right, left -1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            # Make sure we are now on a different column.
            # than the one which we used for top to bottom movement
            if left <= right:
                # Traverse upwards.
                for row in range(bottom, top -1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result