# Given the root of a binary tree, return an array of the largest value
# in each row of the tree (0-indexed).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS soln for level order traversal
        without using deque
        """
        res = []
        row = [root]
        while any(row):
            res.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return res
        