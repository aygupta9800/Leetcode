# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TIme O(logn)
class Solution:
    def successor(self, root):
        """
        one step right and then always left
        """
        root= root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        one step left and then always right:
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        # delete from left
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        #current node
        else:
            # the node is leaf
            if not(root.left or root.right):
                root = None
            # the node is not leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            print(1)
        return root
            