# A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.
# Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. 
# If such an index does not exist, return -1.

#Example
# Input: mat = [[0,0],[0,1]]
# Output: 1


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

#Time complexity O(m+n) space O(1)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        just start from top right
        if 1 move left, if 0 move 1 down
        """
        rows, cols = binaryMatrix.dimensions()
        
        #Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1
        
        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1
                
        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols -1 else -1
        