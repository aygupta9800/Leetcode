# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, s, t):
        if not s and not t: return True
        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and \
            self.isSameTree(s.right, t.right)
        return False
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t: return True
        if not s: return False # t present , s not
        if self.isSameTree(s,t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        