# You want to determine if there is a valid path that exists from vertex start to vertex end.
# Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.


# DFS Soln
# Time Complexity O(V+ E)
# Space complexity O(E)

from collections import defaultdict, deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        neighbors = defaultdict(list)
        #O(E)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        #O(V)    
        def dfs(node, end, seen):
            if node == end:
                return True
            if node in seen:
                return False
            
            seen.add(node)
            for n in neighbors[node]:
                if dfs(n, end, seen):
                    return True
                
            return False
        
        seen = set()    
        return dfs(start, end, seen)


# BFS soln
def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
            
        q = deque([start])
        seen = set([start])
        while q:
            node = q.popleft()            
            if node == end:
                return True            
            for n in neighbors[node]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
                
        return False
    
    #Approach 3 Union Find Soln
    class UnionFind:
        def __init__(self, size):
            self.root = [i for i in range(size)]
            # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
            # The initial "rank" of each vertex is 1, because each of them is
            # a standalone vertex with no connection to other vertices.
            self.rank = [1] * size

        # The find function here is the same as that in the disjoint set with path compression.
        def find(self, x):
            if x == self.root[x]:
                return x
            self.root[x] = self.find(self.root[x])
            return self.root[x]

        # The union function with union by rank
        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.root[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] += 1

        def connected(self, x, y):
            return self.find(x) == self.find(y)

    class Solution:
        def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
            uf = UnionFind(n)
            for u, v in edges: 
                uf.union(u, v)
            return uf.connected(start, end)