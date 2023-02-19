# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites
#  where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.



# Approach 2: Topological sort using kahns algorithm:

# pseudo code for kahn algo
# 1.  start with courses without pre req
#     . Find courses without any incoming edge
# 2. After taking each course, check if we can take other courses:
#     . Remove outgoing edges after taking each course
#     . If a course has no more in-going edge, we can take it

from collections import defaultdict, deque
# time complexity: O(E+V)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        inDegrees = [0 for i in range(numCourses)]

        for next, prev in prerequisites:
            adj[prev].append(next)
            inDegrees[next] += 1

        q = deque([])
        taken = []
        for c in range(numCourses):
            if inDegrees[c] == 0:
                q.append(c)

        while q:
            c = q.popleft()
            # print(c)
            taken.append(c)
            # print(adj[c])
            for nei in adj[c]:
                inDegrees[nei] -= 1
                if inDegrees[nei] == 0:
                    q.append(nei)
        # print(taken)
        return len(taken) == numCourses

# APPROACH 1 : USING DFS:

# IDEA
"""
We make a opposit adj list from course -> list of preReq

then we run dfs for all nodes such that we see if all the prereq are achievable
then the current node is achivable.
if we find a node double in current dfs path i.e. we have cycle.
"""
#code sample 1:
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



# code sample 2:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # opposite Adj list, crs => list(prereq)
        adj = defaultdict(list)
        for crs, prev in prerequisites:
            adj[crs].append(prev)
        
        # maintain a current path visit set for checking cycle
        visit = set()
        def dfs(crs):
            # cycle
            if crs in visit:
                return False
            # all prereq are achievable
            if adj[crs] == []:
                return True

            visit.add(crs)
            for prev in adj[crs]:
                if not dfs(prev):
                    return False
            visit.remove(crs)
            # to not traverse same achievable node again
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True



# -------------------------------------------------------
# DFS Approach 1 to solve the problem
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Keep two set, visited/checked and path
        if node in path return false, if its already checked, return true
        """
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
            if node in visited:
                return True
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            # post order traversal so we have to visit node
            # only after its child/nei are visited
            path.remove(node)
            visited.add(node)
            output.append(node)
            return True
            
        #checking for every node(in case disjoint sets)
        for node in range(numCourses):
            if not dfs(node):
                return []
        return output[::-1]
  