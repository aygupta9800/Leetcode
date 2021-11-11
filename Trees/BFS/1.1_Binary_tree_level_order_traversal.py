# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# node at any level: 

# Approach2 using iteration: Time and space O(n)
# Use queue as data structure i.e deque
# In Python the queue implementation with a fast atomic append() and popleft() is deque.
from collections import deque
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque([root,])
        while queue:
            #start the current level:
            levels.append([])
            #number of elements in the current level(As we run only till current level elem leaving next level elem at the end of iter)
            level_length = len(queue) 
            for i in range(level_length):
                node = queue.popleft()
                #fulfill the current level
                levels[level].append(node.val)
                
                #add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # go to next level
            level += 1
        return levels


# Approach 1 using recursion: 
# Let's first ensure that the tree is not empty, and then call recursively the function helper(node, level),
#  which takes the current node and its level as the arguments.

# NOTE: Time complexity : O(N) since each node is processed exactly once.
# Space complexity : O(N) to keep the output structure which contains N node values.
#Recursive DFS approach
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        def helper(node, level):
            #start the current level:
            if level == len(levels):
                levels.append([])
            #append the current node val
            levels[level].append(node.val)
            
            #process child nodes for next level
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        helper(root, 0)
        return levels

            