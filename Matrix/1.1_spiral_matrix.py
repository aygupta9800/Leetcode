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


# Approach 2:
# mark visited cell with out of range value and keep changing dir till
# 2 times we dont able to move in 2 diff dirn meaning all cell got exhausted
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101 # since val is -100 to 100 so out of range value
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result