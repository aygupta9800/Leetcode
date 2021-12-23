# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
#  A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#  Logic
# At any given node points to note

# 1. If spliting happens at node, none of its child can have split for making path
# 2. If spliting happens at node, that means it is highest order elem in path and there is no parent to it in path

# we will return without split max path sum of node and child to parent 
# and we will update global max path sum with comparing it with branched sum at node
#if negative child value we ignore child subtree for path sum.

#We cant pass global variable in python directly like js
#Time complexity O(n)
# space O(logn) avg recursion height
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            #with split
            res[0] = max(res[0], root.val+ leftMax+ rightMax)
            
            #without split
            return root.val+ max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
        