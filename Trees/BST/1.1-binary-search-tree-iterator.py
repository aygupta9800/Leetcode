# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 2: Controlled Recursion
# space: O(h), tim
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_inorder(root)
        
        
    def left_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    # O(height)
    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self.left_inorder(top.right)
        return top.val

    # time: O(1)
    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()