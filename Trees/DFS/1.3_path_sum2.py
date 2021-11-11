# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
# Each path should be returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity O(n2), debatable: Space complexity O(n2)
#  then there would be N/2N/2 leafs. For every leaf, we perform a potential O(N)O(N) operation of copying over the pathNodes
#  nodes to a new list to be added to the final pathsList. Hence, the complexity in the worst case could be O(N^2)O(N2).
class Solution:
    def helper(self, root, sum, lst, result):
        if root.left is None and root.right is None:
            if root.val == sum:
                result += [lst + [root.val]]
        if root.left:
            self.helper(root.left, sum - root.val, lst+ [root.val], result)
        if root.right:
            self.helper(root.right, sum - root.val, lst+ [root.val], result)
        return result
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return self.helper(root, targetSum, [], [])