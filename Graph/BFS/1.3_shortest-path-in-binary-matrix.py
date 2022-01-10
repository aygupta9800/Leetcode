class Solution:
        def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
            m = len(grid)
            n = len(grid[0])

            # visited = set() #(i, j) 
            if grid[0][0] or grid[n-1][n-1]:
                return -1
            q = deque([(0, 0)]) # i, j
            grid[0][0] = 1
            pathLen = 1
            while len(q):
                qLen = len(q)
                for i in range(qLen):
                    r, c = q.popleft()
                    if r == n-1 and c == n-1:
                        return pathLen
                    # grid[r][c] = 1
                    # visited.add((r, c))
                    lst = [(r-1, c), (r+1, c), (r, c+1), (r, c-1), (r-1, c+1), (r+1, c-1), (r-1, c-1), (r+1, c+1)]
                    for row, col in lst:
                        if 0<=row<m and 0<=col<n and  grid[row][col] == 0:
                            q.append((row, col))
                            grid[row][col] = 1

                pathLen += 1
            return -1

        # time O(m +n)
        # spacEO(m+n)