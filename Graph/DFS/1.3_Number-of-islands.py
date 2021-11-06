# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
#  return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
#  You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        def dfs(grid, r, c):
            grid[r][c] = '0'
            #make nei list to loop
            lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for row, col in lst:
                if row >=0 and col>= 0 and row< len(grid) and col < len(grid[r]) and grid[row][col] == '1':
                    grid[row][col]="0"
                    dfs(grid, row, col)
            
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(grid, r,c)
                    islands += 1
        return islands