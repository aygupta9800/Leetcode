# You are given row x col grid representing a map where grid[i][j] = 1 
# represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely
# surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't
# connected to the water around the island. One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # use marking instead of visit
        # visit = set()
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >=n or grid[r][c] == 0:
                return 1
            
            if grid[r][c] == "#":
                return 0
            
            grid[r][c] = "#"
            
            per = 0
            for row, col in [(r+1, c), (r, c+1), (r-1, c), (r, c-1) ]:
                per+= dfs(row, col)
            
            return per
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return dfs(r, c)
                
        
                    
            
            
        