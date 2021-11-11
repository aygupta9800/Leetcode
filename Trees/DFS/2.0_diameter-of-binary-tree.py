# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        # return Longest path from leaf to root
        def dfs(root):
            if root is None:
                return 0
            left_path = dfs(root.left)
            right_path = dfs(root.right) 
            # No need to add 1 as we are calculating no. of total noded in left/right path so merging r and l path will have diameter equal to child nodes in both
            res[0] = max(res[0], left_path + right_path)
            return max(left_path, right_path)+1
        
        if root is None:
            return 0
        dfs(root)
        return res[0]

        