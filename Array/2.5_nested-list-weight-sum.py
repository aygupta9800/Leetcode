# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Approach 1
# DFS soln
class Solution:
    # BFS SOLN O(n) time O(n) space
    # where N be the total number of nested elements in the input list. 
    # For example, the list [ [[[[1]]]], 2 ] contains 4 nested lists and 2 nested integers (1 and 2), so N=6 for that particular case.
    # space complexity :
    # In the worst case, D=N, (e.g. the list [[[[[[]]]]]]) so the worst-case space complexity is O(N)O(N).
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def depthSum(nested_list, level):
            sm = 0
            for elem in nested_list:
                if elem.isInteger():
                    sm += elem.getInteger() * level
                else:
                    sm += depthSum(elem.getList(), level+ 1)
            return sm
        return depthSum(nestedList, 1)

#Approach2:
# BFS SOLN O(n) time O(n) space 
# The worst-case for space complexity in BFS occurs where most of the elements are in a single layer, for example, a flat list such as [1, 2, 3, 4, 5] as all of the elements must be put on the queue at the same time. Therefore, this approach also has a worst-case space complexity of \mathcal{O}(N)O(N).
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = deque(nestedList)
        depth = 1
        total = 0
        
        while len(q) > 0:
            for i in range(len(q)):
                elem = q.popleft()
                if elem.isInteger():
                    total += elem.getInteger() * depth
                else:
                    q.extend(elem.getList())
            depth += 1
        return total
    
       
        