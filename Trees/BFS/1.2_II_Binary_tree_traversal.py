# Binary Tree Level Order Traversal II
# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (i.e., from left to right, level by level from leaf to root).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach3 Use BFS with 2 queues.
def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels =[]
        if not root:
            return levels
        next_level = deque([root])
        while next_level:
            curr_level= next_level
            next_level = deque()
            #initalize the current level
            levels.append([])
            for node in curr_level:
                levels[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return levels[::-1]

#Approach1: 
# Reverse the top bottom array
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels =[]
        if not root:
            return levels
        q = deque([root,])
        level = 0
        while q:
            qLen = len(q)
            levels.append([])
            for i in range(qLen):
                node = q.popleft()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        levels.reverse()
        return levels

#Recursive DFS approach Approach 2
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
        return levels[::-1]