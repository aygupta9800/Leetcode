#Approach2 Using controlled recursion by stack iterative soln
#Time complexity: Best case: O(1), worst case O(h), Avg case O(1)
# next fn time complexity 
# Space complexity O(h) h= heigh i.e O(logn)
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # self.index = -1
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        ans = self.stack[-1].val
        cur = self.stack.pop()
        if cur.right:
            cur = cur.right
            while cur:
                self.stack.append(cur)
                cur = cur.left
        # self.index += 1
        return ans
        


# Approach 1 time O(N) space O(N) 
# not enough for space constraint
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodesArray = []
        self.index = -1
        self.inorder(root)
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.nodesArray.append(root.val)
        self.inorder(root.right)
        

    def next(self) -> int:
        self.index += 1
        return self.nodesArray[index]
        

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodesArray)
    

