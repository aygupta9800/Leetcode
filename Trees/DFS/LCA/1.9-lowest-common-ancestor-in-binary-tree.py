# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Logic: at lowest anc , there will be splitting such that either of p and q will be different child subtree or one of them is node itself


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res = [None]
        def dfs(curr):
            if not curr:
                return False
            left = dfs(curr.left)
            right = dfs(curr.right)
            mid = curr.val ==p.val or curr.val == q.val
            # print("curr.val",curr.val, "left", left,"==", right, "==", mid)
            if (left and right) or (left and mid) or (right and mid):
                # print("curr.val", curr.val)
                res[0] = curr
            if left or right or mid:
                return True
            return False
        dfs(root)
        return res[0]


# Approach2:
        """
        Aproach2: running dfs with updating ancestor in dfs
        
        """
        leaves = [p, q]
        def dfs(node):
            if not node or node in leaves:
                return node
            L, R = dfs(node.left), dfs(node.right)
            return node if L and R else L or R
        return dfs(root)