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

#Union Find Approach
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        ROWS = len(grid); COLS = len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(ROWS) for j in range(COLS))
        par = [i for i in range(ROWS*COLS)]
        rank = [1]* (ROWS*COLS)
        
        def find(n1):
            root = n1
            while root != par[root]:
                root = par[root]
                
            while par[n1] != root:
                old_root = par[n1]
                par[n1] = root
                n1= old_root
            return root
        
        def union(n1, n2):
            root_n1 = find(n1)
            root_n2 = find(n2)
            if root_n1 == root_n2:
                return False
            if rank[root_n1] > rank[root_n2]:
                par[root_n2] = root_n1
                rank[root_n1] += rank[root_n2]
            else:
                par[root_n1] = root_n2
                rank[root_n2] += rank[root_n1]
            return True
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '0':
                    continue
                index = i*COLS + j
                if j < COLS-1 and grid[i][j+1] == '1' and union(index, index+1):
                    self.count -= 1
                if i < ROWS-1 and grid[i+1][j] == '1' and union(index, index+COLS):
                    self.count -= 1
        return self.count