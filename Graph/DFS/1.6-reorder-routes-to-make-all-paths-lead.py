class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for a, b in connections:
            adj[a].append((b, -1))
            adj[b].append((a, 1))
        
        visit = set()
        count = 0
        def dfs(node):
            nonlocal count
            # if node in visit:
            #     return
            visit.add(node)
            for nei, dr in adj[node]:
                if nei not in visit:
                    # print(dr)
                    
                    if dr == -1:
                        count += 1
                    dfs(nei)
        dfs(0)
        return count
                    
            
            
            