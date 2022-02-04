#Approach 1
# Kahns algorithm:
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(set)
        indegree = defaultdict(int)
        
        for nxt, prev in relations:
            adj[prev].add(nxt)
            indegree[nxt] += 1
            
        canTake = deque([i for i in range(1, n+1) if indegree[i] == 0])
        taken = []
        count = 0
        while canTake:
            count += 1
            qLen = len(canTake)
            for i in range(qLen):
                take = canTake.popleft()
                taken.append(take)
                for i in adj[take]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        canTake.append(i)
        return count if len(taken) == n else -1

# Approach3 : Using dfs for combinig finding cycle 
# and max len calculation, by storing len in visited[node]
#we make visited as hashmap

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        for nxt, prev in relations:
            adj[prev].append(nxt)
        visited = {}
        path = set() # we can mark visited[node] = -1 to tell its in path
        def dfs(node):
            if node in path: # cycle
                return -1
            elif node in visited:
                return visited[node] # dynamic programming. we are removing redundant calculations
            # mark the node as visiting
            path.add(node)
            
            max_len = 1
            for nei in adj[node]:
                length = dfs(nei)
                if length == -1:
                    return -1
                else:
                    max_len = max(length+1, max_len)
            # mark node as visited
            path.remove(node)
            visited[node] = max_len
            return max_len
        
        max_len = -1
        for node in range(1, n+1):
            length = dfs(node)
            if length == -1: # cycle
                return -1
            else:
                max_len = max(length, max_len)
        return max_len


# Approach 2 Using DFS
# 1. Detect cycle 2. find longest dfs path length seperately
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, N + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)

        # check if the graph contains a cycle
        visited = {}

        def dfs_check_cycle(node: int) -> bool:
            # return True if graph has a cycle
            if node in visited:
                return visited[node]
            else:
                # mark as visiting
                visited[node] = -1
            for end_node in graph[node]:
                if dfs_check_cycle(end_node):
                    # we meet a cycle!
                    return True
            # mark as visited
            visited[node] = False
            return False

        # if has cycle, return -1
        for node in graph.keys():
            if dfs_check_cycle(node):
                return -1

        # if no cycle, return the longest path
        visited_length = {}

        def dfs_max_path(node: int) -> int:
            # return the longest path (inclusive)
            if node in visited_length:
                return visited_length[node]
            max_length = 1
            for end_node in graph[node]:
                length = dfs_max_path(end_node)
                max_length = max(length+1, max_length)
            # store it
            visited_length[node] = max_length
            return max_length

        return max(dfs_max_path(node)for node in graph.keys())
                
                        
        
        