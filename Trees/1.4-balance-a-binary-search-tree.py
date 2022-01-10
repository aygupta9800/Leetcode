# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []
        """
        Use inorder traversal to get sorted array of BST
        """
        def inOrder(node):
            if node:
                inOrder(node.left)
                res.append(node.val)
                inOrder(node.right)
        inOrder(root)
        """
        Use divide and conquer to make a balance tree
        We can also store node itself rather than node val to not create any extra new tree nodes
        """
        def divideAndBalance(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(res[mid])
            node.left = divideAndBalance(left, mid -1) 
            node.right = divideAndBalance(mid +1, right)
            return node
        
        return divideAndBalance(0, len(res) -1)
            