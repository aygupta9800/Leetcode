

#Approach2 Using postorder Traversal:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Serialization could be easily implemented with both strategies, but for optimal
deserialization better to choose the postorder traversal because
member/global/static variables are not allowed here.
"""

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + \
                [root.val] if root else []
        
        return ' '.join(map(str, postorder(root)))
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def dfs(low=float('-inf'), high=float('inf')):
            if not data or data[-1] < low or data[-1] > high:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = dfs(val, high)
            root.left = dfs(low, val)
            return root
        data = [int(x) for x in data.split(' ') if x]
        return dfs()

# Approach 1 Using BFS with delimeter
from collections import deque
class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        tree = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                tree.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                tree.append('*')
        return ','.join(tree)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        tree = deque(data.split(','))
        root = TreeNode(int(tree.popleft()))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # := is assignment operator
            if (left := tree.popleft()) != '*':
                node.left = TreeNode(int(left))
                queue.append(node.left)
            
            if (right := tree.popleft()) != '*':
                node.right = TreeNode(int(right))
                queue.append(node.right)
                
        return root