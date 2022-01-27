# Given the root of a binary tree, the value of a target node target, and an integer k,
# return an array of the values of all nodes that have a distance k
# from the target node.

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# You can return the answer in any order.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Approach2 : Percolate distance
# Time: O(n), space(O(n))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1 approach Percoalte Distance
# 1 put every node with info of parent, 2nd do bfs search from target to find the answer
#Time: O(n), space(O(N))

class Solution:
    """
    1.From root, say the target node is at depth 3 in the left branch.
    It means that any nodes that are distance K - 3 in the right branch should be added to the answer.
    2. also we need to add nodes at k dist from subtree starting at target
    """
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        
        # Return distance from node to target if exists else -1
        # vertex distance: the # of vertices on the path form node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 0 #here is node is same as target we return dist 0
            else:
                L, R = dfs(node.left), dfs(node.right)
                
                #means target is in left side of node
                if L != -1:
                    if L+1== k: # L+1 will be distance of node from target
                        res.append(node.val)
                    subtree_add(node.right, L+2) #node.right will be at dist L+2
                    return L+1
                #means target is in right side of node
                elif R != -1:
                    if R +1 == k:
                        res.append(node.val)
                    subtree_add(node.left, R+2)
                    return R+1
                # target is not part of subtree from current node
                else:
                    return -1
                
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == k:
                res.append(node.val)
            else:
                subtree_add(node.left, dist+1)
                subtree_add(node.right, dist+1)

        dfs(root)
        return res
        

#  Approach 1: Annonate Parent
# 1 put every node with info of parent, 2nd do bfs search from target to find the answer
#Time: O(n), space(O(N))

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par= None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root)
        
        # Traversing from target as if tree was graph
        q = deque([(target, 0)])
        visit = {target}
        
        while q:
            # when we reach k distance
            if q[0][1] == k:
                return [node.val for node, d in q]
            
            node, d = q.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in visit:
                    visit.add(nei)
                    q.append((nei, d+1))
        return []
            
        