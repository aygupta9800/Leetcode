# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
#         shortest path with bfs
        if not root:
            return None
        mindist = float("inf")
        ans = None
        def dfs(node):
            nonlocal ans, mindist
            if node is None:
                return -1
            if node.val == k:
                subtree(node, 0)
                return 0
            if node.left is None and node.right is None:
                return -1
            L, R = dfs(node.left), dfs(node.right)
            if L != -1:
                if node.right is not None:
                    subtree(node.right, L+2)
                return L+1
            elif R != -1:
                if node.left is not None:
                    subtree(node.left, R+2)
                return R+1
            return -1
        
        def subtree(node, dist):
            nonlocal ans, mindist
            if node.left is None and node.right is None:
                if dist < mindist:
                    ans = node.val
                    mindist = dist
                return
            if node.left:
                subtree(node.left, dist+1)
            if node.right:
                subtree(node.right, dist+1)
        dfs(root)
        return ans

# Soln 2 convert to graph and then bfs
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = collections.defaultdict(list)
        q = collections.deque([])
        def dfs(node, par = None):
            if node:
                if node.val == k:
                    q.append(node)
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        # queue = collections.deque(node for node in graph
        #                           if node and node.val == k)
        seen = set(q)

        while q:
            node = q.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
        