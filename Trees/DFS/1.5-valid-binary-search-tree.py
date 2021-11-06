# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, low , high):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            return dfs(node.left, low,node.val) and dfs(node.right, node.val, high)
        
        # return dfs(root, -math.inf, math.inf)
        return dfs(root, -sys.maxsize, sys.maxsize)

#iterative appraoch
#  def isValidBST(self, root: TreeNode) -> bool:
#         if not root:
#             return True

#         stack = [(root, -math.inf, math.inf)]
#         while stack:
#             root, lower, upper = stack.pop()
#             if not root:
#                 continue
#             val = root.val
#             if val <= lower or val >= upper:
#                 return False
#             stack.append((root.right, val, upper))
#             stack.append((root.left, lower, val))
#         return True
