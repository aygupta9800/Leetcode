# TIme complexity O(n) since each node is processed exactly once.
# spcae complexity O(n) We have to keep a recursion stack of the size of the tree height, which is \mathcal{O}(\log N)O(logN) for the best case of completely balanced tree and \mathcal{O}(N)O(N) for the worst case of completely unbalanced tree.
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
       
        """
        Perform standard in-order traversal :
        left -> node -> right
        and link all the nodes into DLL
        """
        def dfs(node):
            nonlocal first, last
            if not node:
                return
            dfs(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            dfs(node.right)
        
        if not root:
            return None
        
        first, last = None, None
        dfs(root)
        last.right = first
        first.left = last
        return first
  