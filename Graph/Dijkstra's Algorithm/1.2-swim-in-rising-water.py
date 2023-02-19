class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Use Dijkestra to know the min cost to reach from a to b in directed graph
        minHeap = [(grid[0][0], 0, 0)]
        m, n = len(grid), len(grid[0])
        visit = set((0,0))
        t = 0
        while minHeap:
            cost, i, j = heapq.heappop(minHeap)
            if i == m-1 and j == n-1:
                return cost
            # t = max(t, cost)
            t = cost
            for a,b in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                r, c = i+a, j +b
                if 0<=r< m and 0<=c<n and (r,c) not in visit:
                    # we are taking node value in consideration during pushing so no need to take max of cost and t at poping
                    heapq.heappush(minHeap, (max(grid[r][c], cost), r, c))
                    visit.add((r,c))
        return -1
                    
            