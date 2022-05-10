# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        Keep a pointer to cur index till we have traversed, and dummy pointer to track head. to avoid cycle dont forget to change left point of root to null
        
        """
        dummy = TreeNode(0)
        cur = dummy
        def dfs(root):
            nonlocal cur
            if root is None:
                return
            dfs(root.left)
            cur.right= root
            cur = cur.right
            root.left = None
            dfs(root.right)
        dfs(root)
        return dummy.right
        
        