#Approach2 Using Kanhns algo
# soln1 Time O(V+E), Space O(V+E)
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        inDegrees = [0 for i in range(numCourses)]
        outGoing = defaultdict(list)
        
        for i, j in prerequisites:
#              j -> i
            outGoing[j].append(i)
            inDegrees[i] += 1
        
        # canTake = [i for i in range(numCourses) if inDegrees[i] == 0]
        canTake = deque([])
        for i in range(numCourses):
            if inDegrees[i] == 0:
                canTake.append(i)
        
        taken = []
        
        while len(canTake) > 0:
            node = canTake.popleft()
            taken.append(node)
            for nei in outGoing[node]:
                inDegrees[nei] -= 1
                if inDegrees[nei] == 0:
                    canTake.append(nei)
        
        return taken if len(taken) == numCourses else []

# APPROACH-2 Using DFS:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # opposite Adj list, crs => list(prereq)
        adj = defaultdict(list)
        for crs, prev in prerequisites:
            adj[crs].append(prev)
        
        # maintain a current path visit set for checking cycle
        visit = set()
        # a set for taken nodes so that we can know if pre crs is taken before
        takenSet = set()
        takenOutput = []
        def dfs(crs):
            # cycle
            if crs in visit:
                return False
            # already taken
            if crs in takenSet:
                return True

            # put node in current path and explore prereq
            visit.add(crs)
            for prev in adj[crs]:
                if not dfs(prev):
                    return False
            # remove node from current path and add in taken output and set
            visit.remove(crs)
            takenSet.add(crs)
            takenOutput.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return takenOutput

 
# soln2
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
            
         