# DFS Soln
# Time Complexity: O(N + E)O(N+E), where NN is the number of nodes in the graph, and EE is the number of edges. We explore each node once when we transform it from uncolored to colored, traversing all its edges in the process.

# Space Complexity: O(N)O(N), the space used to store the color.


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #dfs soln
        #with recursion
        color = {}
        def dfs(node):
            if node not in color:
                color[node] = 0
            for nei in graph[node]:
                if nei not in color:
                    color[nei] = 0 if color[node] == 1 else 1
                    if not dfs(nei):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True
        
        for node in range(len(graph)):
            if not dfs(node):
                return False
        return True


# Using Stack
class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True