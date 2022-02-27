# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Time : O(n), space: O(height) => O(logn) for balanced tree
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, maxVal):
            nonlocal count
            if not node:
                return 
            if node.val >= maxVal:
                count += 1
                maxVal = node.val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, float('-inf'))
        return count