# Approach 1 DFS O(n) time O(n) space
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            nonlocal res
            if node:
                path = path + str(node.val)
            
                if not node.left and not node.right:
                    res += int(path)
                dfs(node.left, path)
                dfs(node.right, path)
        dfs(root, "0")
        return res

# Approach 2: Morris Preorder Traversal
# TIme O(N) SpaceO(1)
def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        path  = "0"
        # morrison PreOrder Traversal
        while root:
            # If there is left child find root left predecessor
            # If there is no predecessor.right = root link --> set it
            # If there is a link predecessor.right = root --> break it
            if root.left:
                predecessor = root.left
                # go as right as you can
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1
                 
                # set link predecessor.right = root and explore left subtree
                if predecessor.right is None:
                    path = path + str(root.val)
                    predecessor.right = root
                    root = root.left
                    
                # Break the link predecessor.right = root and explore the right subtree
                else:
                    """
                    If it was inorder traversal then we would have visited root in this
                    """
                    # if you are on the leaf, update the sum
                    if predecessor.left is None:
                        res += int(path)
                    # this part of the tree is explored, backtrack
                    path = path[:-steps]
                    predecessor.right = None
                    root = root.right
            else:
                path = path + str(root.val)
                # If you are on leaf, update the sum
                if root.right is None:
                    res += int(path)
                root = root.right
        return res
           
