# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges 
# where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

#Time complexity O(N⋅α(N)) alpah(n) is inverse Ackerman soln
# Time Complexity : O(N⋅α(N)).
# When E ≠ N - 1, E=N−1, we simply return false. Therefore, the worst case is when E=N−1. Because E is proportional to N, we'll say E = NE=N to simplify the analysis.
# We are putting each of the NN edges into the UnionFind data structure, using the union(...) method. The union(...) method itself has no loops or recursion, so the entire cost of calling it is dependent on the cost of the find(...) method that it calls.
# find(...)'s cost is dependent on how far the node it was searching for is from the root. Using the naïve implementation of union find, this depth could be NN. If this was the case for all of the calls, 
# we'd have a final cost of O(N^2)O(N 2).

# However, remember those optimizations we did? Those keep the tree depths very shallow. It turns out that find(...) amortizes to O(α(N))O(α(N)), where α is the Inverse Ackermann Function. The incredible thing about this function is that it grows so slowly that NN will never go higher than 44 in the universe as we know it! So while in "practice" it is effectively O(1)O(1), in "theory" it is not.
# Actually proving this upper bound on the depth is a very advanced proof, which I'd certainly hope you'd never need to do in an interview! If you're interested though, I recommend looking in a good algorithm's text book or paper.

# Anyway, this gives us a total of N \cdot O(α(N)) = O(N \cdot α(N))N⋅O(α(N))=O(N⋅α(N)).
# Space Complexity : O(N).
# The UnionFind data structure requires O(N)O space to the store the arrays it uses.

# Union find with optimization path compression and union by size
class UnionFind:
    
    # For efficiency, we aren't using makeset, but instead initialising
    # all the sets at the same time in the constructor.
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        # We use this to keep track of the size of each set.
        self.size = [1] * n
        
    # The find method, with path compression. There are ways of implementing
    # this elegantly with recursion, but the iterative version is easier for
    # most people to understand!
    def find(self, A):
        # Step 1: Find the root.
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        # Step 2: Do a second traversal, this time setting each node to point
        # directly at A as we go.
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root
        
    # The union method, with optimization union by size. It returns True if a
    # merge happened, False if otherwise.
    def union(self, A, B):
        # Find the roots for A and B.
        root_A = self.find(A)
        root_B = self.find(B)
        # Check if A and B are already in the same set.
        if root_A == root_B:
            return False
        # We want to ensure the larger set remains the root.
        if self.size[root_A] < self.size[root_B]:
            # Make root_B the overall root.
            self.parent[root_A] = root_B
            # The size of the set rooted at B is the sum of the 2.
            self.size[root_B] += self.size[root_A]
        else:
            # Make root_A the overall root.
            self.parent[root_B] = root_A
            # The size of the set rooted at A is the sum of the 2.
            self.size[root_A] += self.size[root_B]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False
        
        # Create a new UnionFind object with n nodes. 
        unionFind = UnionFind(n)
        
        # Add each edge. Check if a merge happened, because if it 
        # didn't, there must be a cycle.
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        
        # If we got this far, there's no cycles!
        return True


#Approach 2 

#Union Find
class UnionFind:

    # We dont need to maintain multiple sets for linked nodes, we can just maintain parent root node for each index to know
    # they are in same connected component
    def __init__(self, n):
        self.parent = [node for node in range(n)]
    
    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]
        return A
    
    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        
        if root_A == root_B:
            #Cycle formed
            return False 
        self.parent[root_A] = root_B
        return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        
        unionFind = UnionFind(n)
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        return True
                       

# -----------------



# Logic:
# For graph to be true, after dfs there should be no cycles so we keep prev elem track to avoid false positive
# and whole graph should be connected that is no. of nodes = no. of visited node

# DFS
# Time complexity O(n+ edges), space O(n)
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
        
        # We need previous element to remove false positive of having a cycle when we again found prev elem in visit set
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
                
                
        