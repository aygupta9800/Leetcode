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

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Taking set here as removing edge from set will be of constant time
        """
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
                inGoing[nextCourse].remove(take) # remove ingoing edge of nextcourse
                if len(inGoing[nextCourse]) == 0: # add nextcourse if no edge
                    canTake.append(nextCourse)
        # print(taken)
        return len(taken) == numCourses


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
  