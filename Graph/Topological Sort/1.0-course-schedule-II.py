#Approach2 Using Kanhns algo
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inGoing = defaultdict(set)
        outGoing = defaultdict(set)
        for i,j  in prerequisites:
            # j is pre req of i i.e j -> i
            inGoing[i].add(j)
            outGoing[j].add(i)
        canTake = [i for i in range(numCourses) if len(inGoing[i]) == 0]
        taken = []
        while len(canTake) > 0:
            take = canTake.pop()
            taken.append(take)
            for nextCourse in outGoing[take]:
                inGoing[nextCourse].remove(take)
                if len(inGoing[nextCourse]) == 0:
                    canTake.append(nextCourse)
        # print(taken)
        return taken if len(taken) == numCourses else []

#Approach1 Using post order DFS
    """
    The rationale is that given a node, if the subgraph formed by all
    descendant nodes from this node has no cycle, then adding this node
    to the subgraph would not form a cycle either.
    """
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #building adj list from pre -> next
        adj = defaultdict(list)
        for nxt, prev in prerequisites:
            adj[prev].append(nxt)
            
        # a course has 3 possible states:
        # visited -> crs has been checked and added to output
        # visiting -> In current dfs path, but not in output
        # unvisited -> crs not been seen at all
        
        output = []
        # path represents if node in current path
        # checked means its already checked
        visited, path = set(), set()
        #postorder DFS
        def dfs(node):
            # cycle detected
            if node in path:
                return False
            # if the path for this node is already checked no need to check it again
            if node in visited:
                return True
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            visited.add(node)
            output.append(node)
            return True
            
        #checking for every node(in case disjoint sets)
        for node in range(numCourses):
            if not dfs(node):
                return []
        return output[::-1]
            
         