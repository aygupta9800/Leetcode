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
        print(taken)
        return len(taken) == numCourses


# -------------------------------------------------------
# DFS Approach 1 to solve the problem
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency list maping each course to its pre req list
        preMap = { i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        #Visit set = all the courses along the curr DFS path 
        visitSet = set()
        
        #no need for prev as directed graph
        def dfs(crs):
            #loop detect as its in visitset for a current dfs path
            if crs in visitSet:
                return False
            if preMap[crs] ==[]:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # directed graph so crs can be neigbhour of others but not necessary vice-versa so to avoid false cycle positive         
            visitSet.remove(crs)
            # so that next dfs on same crs save same steps
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True