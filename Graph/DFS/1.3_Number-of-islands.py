# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
#  return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
#  You may assume all four edges of the grid are all surrounded by water.

# Complexity Analysis

# Time complexity : O(M×N) where M is the number of rows and N is the number of columns.

# Space complexity : worst case O(M \times N)O(M×N) in case that the grid map is filled with lands where DFS goes by M \times NM×N deep.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        def dfs(grid, r, c):
            grid[r][c] = '0'
            #make nei list to loop
            lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for row, col in lst:
                if row >=0 and col>= 0 and row< len(grid) and col < len(grid[r]) and grid[row][col] == '1':
                    # grid[row][col]="0"
                    dfs(grid, row, col)
            
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(grid, r,c)
                    islands += 1
        return islands

#Union Find Approach
# Time complexity : O(M×N) where M is the number of rows and N is the number of columns. Note that Union operation takes essentially constant time[1] when UnionFind is implemented with both path compression and union by rank.

# Space complexity : O(M×N) as required by UnionFind data structure.
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

# Complexity Analysis
# Time complexity : O(M×N) where MM is the number of rows and NN is the number of columns.

# Space complexity : O(min(M, N))O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N).
# BFS soln:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        ROWS, COLS = len(grid), len(grid[0])
        if not ROWS: return 0
        q = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    grid[r][c] = 0
                    q.append((r,c))
                    self.bfs(grid, q, ROWS, COLS)
                    islandCount += 1
        return islandCount
    def bfs(self, grid, q, ROWS, COLS):
        while q:
            r,c = q.popleft()
            for row, col in ((r-1,c), (r+1, c), (r, c+1), (r, c-1)):
                if row >=0 and col >=0 and row <ROWS and col <COLS and grid[row][col]== '1':
                    q.append((row, col))
                    grid[row][col] = 0