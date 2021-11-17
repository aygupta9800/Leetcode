# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        
        #
        ROWS, COLS = len(grid), len(grid[0])
        fresh_oranges = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges +=1
        
        if fresh_oranges == 0 : return 0
        
                    
        minutes = -1
        while q:
            minutes += 1
            qLen = len(q)
            for i in range(qLen):
                r,c = q.popleft()
                lst = [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]
                for row, col in lst:
                    if row >=0 and col >=0 and row < ROWS and col < COLS and grid[row][col]==1:
                        grid[row][col] = 2
                        fresh_oranges -= 1
                        q.append((row, col))
        return minutes if fresh_oranges == 0 else -1
        
        
                    