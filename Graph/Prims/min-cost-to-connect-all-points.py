# Return the minimum cost to make all points connected. All points are connected
#  if there is exactly one simple path between any two points.

# Ex.
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

# Approach1 : Prims algo
# Time Complexity O(n2 *logn)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        
        # forming adj list
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2)+ abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        #Prims
        res = 0
        visit = set()
        minH = [(0, 0)] #(cost, point) #frontier
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            # even if point is already in heap, we again push it in case we have a shorter edge cost with current point
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
                    
        return res
        