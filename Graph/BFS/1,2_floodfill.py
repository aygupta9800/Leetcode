# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.

#DFS Soln
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r,c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >=1 : dfs(r-1, c)
                if r+1 <ROWS : dfs(r+1, c)
                if c >=1 : dfs(r, c-1)
                if c+1 < COLS: dfs(r, c+1)
                    
        dfs(sr,sc)
        return image

# Need visit set as old color can be same as new color
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
                
                
        