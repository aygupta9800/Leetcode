# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time Complexity:O(N+M), where N is a number of nodes (vertices) and M is a number of edges.
# Space Complexity: O(N). This space is occupied by the visited hash map and in addition to that, space would also be occupied by the recursion stack since we are adopting a recursive approach here. The space occupied by the recursion stack would be equal to O(H) where H is the height of the graph. Overall, the space complexity would be O(N).

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val, [])
            # to avoid cycles       
            oldToNew[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None

#  BFS soln
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
         # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        if not node:
            return None
        oldToNew = {}
        q = deque([node])
        copy = Node(node.val, [])
        oldToNew[node] = copy
        
        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val, [])
                    q.append(nei)
                oldToNew[n].neighbors.append(oldToNew[nei])
        return oldToNew[node] if node else None
        

        
        