# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.



from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        q = deque([(sr, sc)])
        visitset= set((sr,sc))
        while q:
            r,c = q.popleft()
            image[r][c] = newColor

            lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for row, col in lst:
                if (row, col) not in visitset and row>=0 and col>=0 and row< len(image) and col< len(image[0]) and image[row][col] == oldColor:
                    visitset.add((row, col))
                    q.append((row, col))
        return image
                
                
        