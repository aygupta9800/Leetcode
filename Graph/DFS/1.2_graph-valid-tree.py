# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges 
# where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Logic:
# For graph to be true, after dfs there should be no cycles so we keep prev elem track to avoid false positive
# and whole graph should be connected that is no. of nodes = no. of visited node

# DFS
# Time complexity O(n+ edges), space O(n + E)
# Time Complexity : O(N + E)O(N+E).
# Creating the adjacency list requires initialising a list of length NN, with a cost of O(N), and then iterating over and inserting EE edges, for a cost of O(E). This gives us O(E) + O(N)= O(N+E).
# Each node is added to the data structure once. This means that the outer loop will run N times. For each of the N nodes, its adjacent edges is iterated over once. In total, this means that all E edges are iterated over once by the inner loop. This, therefore, gives a total time complexity of O(N+E).
# Because both parts are the same, we get a final time complexity of O(N+E).

# Space Complexity : O(N+E).
# The adjacency list is a list of length NN, with inner lists with lengths that add to a total of E. This gives a total of O(N+E) space.
# In the worst case, the stack/ queue will have all NN nodes on it at the same time, giving a total of O(N) space.
# In total, this gives us O(E+N) space.



#Depth-first search is a classic graph-traversal algorithm that can be used to check for both of these conditions:
# G is fully connected if, and only if, we started a depth-first search from a single source and discovered all nodes in G during it.
# G contains no cycles if, and only if, the depth-first search never goes back to an already discovered node. We need to be careful though not to count trivial cycles of the form A → B → A that occur with most implementations of undirected edges.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
#         or default dict
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
                
            return True
        
        return dfs(0, -1) and n == len(visit)

# Iterative DFS using stack
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # Visited map
    parent = {0: -1}
    stack = [0]
    
    while stack:
        node = stack.pop()
        for neighbour in adj_list[node]:
            if neighbour == parent[node]:
                continue
            if neighbour in parent:
                return False
            parent[neighbour] = node
            stack.append(neighbour)
    
    return len(parent) == n

# Iterative BFS
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    parent = {0: -1}
    queue = collections.deque([0])
    
    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if neighbour == parent[node]:
                continue
            # To detect cycle
            if neighbour in parent:
                return False
            parent[neighbour] = node
            queue.append(neighbour)
    # whether graph is connected
    return len(parent) == n
                
                
        