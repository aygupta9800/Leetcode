# APproach 1 Using Queue
# Time complexity O(m*n), space O(m*n)
class Solution:
    """
    Rather running dfs from every grid cell, we run it from ends of grid and check
    which cell we can reach for pacifc, and for atlantic. Then we take intersection.
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit):
            visit.add((r,c))
            lst = [(r+1, c), (r-1,c), (r, c+1), (r, c-1)]
            for row, col in lst:
                # in bound
                if row <0 or col<0 or row>=m or col>=n:
                    continue
                # in visit or nei should have more or same height
                if (row, col) in visit or heights[r][c] > heights[row][col]:
                    continue
                dfs(row, col, visit)
                
        # loop through each adj cell to oceans
        for c in range(n):
            dfs(0, c, pac)
            dfs(m-1, c, atl)
            
        for r in range(m):
            dfs(r, 0, pac)
            dfs(r, n-1, atl)
            
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res


# Approach2 Using BFS:
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacQ, atlQ = deque(), deque()
        
        # loop through each adj cell to oceans
        for c in range(n):
            pacQ.append((0, c))
            atlQ.append((m-1, c))
            
        for r in range(m):
            pacQ.append((r, 0))
            atlQ.append((r, n-1))
            
        def bfs(q):
            visit = set()
            while q:
                (r,c) = q.popleft()
                visit.add((r,c))
                
                for row, col in [(r+1,c), (r-1,c), (r, c+1), (r, c-1)]:
                    if row<0 or row>=m or col<0 or col>=n \
                    or (row, col) in visit or heights[row][col] <heights[r][c]:
                        continue
                    q.append((row, col))
            return visit
                
        pac, atl = bfs(pacQ), bfs(atlQ) 
            
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res