#Approach 2: Reversing first across diagonal then from left to right in a row
# Time complexity: O(number of cell), Space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        Rotating the n*n square matrix = 
        1. (Transpose) First reverse the matrix around main diagonal i.e a[i][j] swaped with a[j][i]
        2. (Reflect) Reverse matrix from left to right
        Does twice as many reads and write then rotating around cells but same time and space complexity
        easier to read and code and can be found custom library function 
        """

        self.transpose(matrix)
        self.reflect(matrix)
    

    def transpose(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reflect(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j  in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-j-1], matrix[i][j]

# Approach 1: Roatating cells in corners
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) -1
        
        while left < right:
            top, bottom = left, right
            # Imp step as we need measure of change from left pos for calculation
            # we use i in range(right-left) rather than (left, right)
            for i in range(right-left):
                #save the topleft
                topLeft =matrix[top][left+ i]

                #move bottom left into top left
                matrix[top][left+i] = matrix[bottom - i][left]

                #move bottom right into bottom left
                matrix[bottom -i][left] = matrix[bottom][right - i]

                #move top right into bottom right
                matrix[bottom][ right-i] = matrix[top+ i] [right]

                #move top left into top right
                matrix[top+i][right] = topLeft
            left += 1
            right -= 1
        
