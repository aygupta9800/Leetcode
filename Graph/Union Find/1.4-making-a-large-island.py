# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.

# Logic

# since we need to find a zero such that when we turn it 1 it joins two or more island
# to overall increase size of island, we need to keep track of islands and their
# sizes. Using Union Find we can find all the islands and their Size
# later we keep a visited set for every 0 cell to check how many different island
# are their near that cell. we add up all of their sizes + 1(0 cell itself)
# and in last we keep track of max of all such sizes


# TIme complexity O(m*n)= O(n2) as m =n
# space O(n2) to store size and parent
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        0 0 0
        1 1 0
        0 0 1
        Gonna use Union Find approach so not to keep track of index of islands
        """
        m, n = len(grid), len(grid[0])
        
        par = [i for i in range(m*n)] # list(range(m*n))
        size = [1] * (m*n)
        
        def find(x):
            root = x
            while root != par[root]:
                root = par[root]
            while par[x] != root:
                old_root = par[x]
                par[x] = root
                x = old_root
            return root
        
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 == r2:
                return False
            if size[r1] > size[r2]:
                par[r2] = r1
                size[r1] += size[r2]
            else:
                par[r1] = r2
                size[r2] += size[r1]
            return True
        
        # 4 direction
        # direction = [(0, -1), (-1, 0),(0, 1), (1, 0)]
        # build the islands
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # just consider left and top elem as we are scan L to R, Top to Bottom
                    for row, col in [(r-1, c), (r, c-1)]:
                        if  0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                            union(r*m+c, row*m+col)
        
        #Try each 0 cell:
        ans = 0
        has_zeroes = False
        print(par)
        print(size)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    has_zeroes = True
                    visited = set()
                    total = 1 # considering we turn this c=0 cell to 1
                    for row, col in [(r-1,c),(r+1, c), (r, c-1), (r, c+1)]:
                        if  0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                            key = row* m + col
                            root = find(key)
                            if root not in visited:
                                # print(root)
                                # print(par)
                                # print(size)
                                total += size[root]
                                visited.add(root)
                    ans = max(ans, total)
        return ans if has_zeroes else m*n
                            
                        
                
        
                
            
                
        