# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, path):
            path += str(root.val)
            if not root.left and not root.right:
                res.append(path)
                return
            else:
                path += "->"
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
        
        dfs(root, "")
        if not root:
            return []
        return res