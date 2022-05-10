# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach2:
"""
1. Using BFS find the first and last node of the deepest leave
2. find lowest common ancestor of first and last node.
"""
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            q = deque([root])
            while q:
                levels =[]
                levels.extend([q[0], q[-1]])
                qlen = len(q)
                for i in range(qlen):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if not q:
                    return levels
        deepestLeafs = bfs(root)
        def LCA(node):
            if not node or node in deepestLeafs:
                return node
            L, R = LCA(node.left), LCA(node.right)
            return node if L and R else L or R
        return LCA(root)
        
#O(n)
# Approach1
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        lowest common ancestor of deepest leaves
        1. pass find all deepest node of tree using dfs
        2. find lowest common ancestor using logic:
            a: if node is of max depth or none , returns node
            b: if both left and right has some answer, return current node
            c: else return answer(node.left) or answer(node.right)
        
        """
        # Tag each node with its depth
        maxdepth = -1
        deepestLeaves = set()
        
        def dfs(node, depth):
            nonlocal maxdepth, deepestLeaves
            if node:
                if depth > maxdepth:
                    maxdepth = depth
                    deepestLeaves = set([node])
                elif depth == maxdepth:
                    deepestLeaves.add(node)
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        dfs(root, 0)
        # print("deepest leaves", deepestLeaves)  
        # now use another function for finding lowest common ancestor
        def LCA(node):
            if not node or node in deepestLeaves:
                return node
            L, R = LCA(node.left), LCA(node.right)
            return node if L and R else L or R
        return LCA(root)
        