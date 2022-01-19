

#Approach2 dfs soln Time:O(n) SpaceO(1)
class Solution:
    def flatten(self, node: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        if we track tail of every subtree, we can attach it to next right
        subtree in link list.
        """
        # for no node, no tail
        if not node:
            return None
        
        # for single node, tail is itself
        if not node.left and not node.right:
            return node
        
#         flat left subtree
        leftTail = self.flatten(node.left)
        rightTail = self.flatten(node.right)
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        # return rightTail or leftTail or root
        return rightTail if rightTail else leftTail

# Approach 3 using stack

#Approach 1 dfs My soln
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            if root.left:
                last = dfs(root.left)
            else:
                last = root
            last.right = root.right
            if root.right:
                last= dfs(root.right)
            if root.left:
                root.right = root.left
            root.left = None
            return last
        dfs(root)
