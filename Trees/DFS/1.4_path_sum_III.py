# Given the root of a binary tree and an integer targetSum, return the number of paths
#  where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, 
# but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def helper(self, root, sum, lst, count):
        lst.append(root.val)
        if root.left:
            count = self.helper(root.left, sum, lst, count)
        if root.right:
            count = self.helper(root.right, sum, lst, count)
        """
        The trick is to check the sum of path from bottom node to current node and check how many can have same sum
        """
        temp = 0
        for i in range(len(lst)-1, -1, -1):
            temp += lst[i]
            if temp == sum:
                count +=1
        lst.pop()
        return count
     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        return self.helper(root, targetSum, [], 0)
        