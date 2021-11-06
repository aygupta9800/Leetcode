# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left= right= []
        def dfs(node1, node2):
            if not node1:
                return True if not node2 else False
            if not node2:
                return False
            if node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left):
                return True
            return False
        
        return dfs(root.left, root.right)