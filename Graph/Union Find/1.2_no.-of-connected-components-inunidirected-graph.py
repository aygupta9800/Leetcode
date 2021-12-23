# 323. Number of Connected Components in an Undirected Graph
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge
#  between ai and bi in the graph. Return the number of connected components in the graph.
#  With union find path compression and size optimization
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        #size
        rank = [1]*n
        
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
        
        #Initial total set
        count = n
        for n1, n2 in edges:
            if union(n1, n2):
                count -= 1
        
        return count

        #Approach 2: with DFS
    #TIme complexity 
#     Complexity Analysis
# Here EE = Number of edges, VV = Number of vertices.
# Time complexity: O(E+V).
# Building the adjacency list will take O(E) operations, as we iterate over the list of edges once, and insert each edge into two lists.
# During the DFS traversal, each vertex will only be visited once. This is because we mark each vertex as visited as soon as we see it, and then we only visit vertices that are not marked as visited. In addition, when we iterate over the edge list of each vertex, we look at each edge once. This has a total cost of O(E+V).
    
#     Space complexity: O(E+V).

# Building the adjacency list will take {O}(E)O(E) space. To keep track of visited vertices, an array of size O(V) is required. Also, the run-time stack for DFS will use O(V) space.
    class Solution:
        def countComponents(self, n: int, edges: List[List[int]]) -> int:
            if not n:
                return 0
            
            adj = collections.defaultdict(list)
            for i ,j in edges:
                adj[i].append(j)
                adj[j].append(i)
                
            visit = set()
            
            def dfs(node):
                if node in visit:
                    return False
                visit.add(node)
                for nei in adj[node]:
                    if nei not in visit:
                        dfs(nei)
                # visit.remove(node)
                return True
            count = 0
            for i in range(n):
                if dfs(i):
                    count += 1
            return count
                
        
                