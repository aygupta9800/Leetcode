# Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

# There are several ways to implement the BFS algorithm.
# 1.One way would be that we run a two-level nested loop, with the outer loop iterating each level on the tree,
# and with the inner loop iterating each node within a single level.

# 2. We could also implement BFS with a single loop though. The trick is that we append the nodes to be visited into a queue 
# and we separate nodes of different levels with a sort of delimiter (e.g. an empty node). The delimiter marks the end of a level, as well as the beginning of a new level.

# Approach 2: with single loop BFS
# Alternate order of insertion with adding delimeter
# Time complexity O(n)
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    ret = []
    # We maintain a queue for storing current level elements during traversal
    level_list = deque()
    if root is None:
        return []
    # start with level 0 with a delimeter
    node_queue = deque([root, None])
    is_order_left = True
    
    while len(node_queue) > 0:
        curr_node = node_queue.popleft()
        if curr_node:
            if is_order_left: 
                level_list.append(curr_node.val)
            else:
                level_list.appendleft(curr_node.val)
            if curr_node.left:
                node_queue.append(curr_node.left)
            if curr_node.right:
                node_queue.append(curr_node.right)
        else:
            # we finish one level
            ret.append(level_list)
            #add a delimeter to mark the level
            if len(node_queue) > 0:
                node_queue.append(None)
                
            #prepare for the next level
            level_list = deque()
            is_order_left = not is_order_left
    return ret


# DFS Approach
# The trick is that during the DFS traversal, we maintain the results in a global array that is indexed by the level, i.e. the element array[level] would contain all the nodes that are at the same level.
#  The global array would then be referred and updated at each step of DFS.
# We define a recursive function called DFS(node, level) which only takes care of the current node which is located at the specified level. Within the function, here are three steps that we would perform:
# If this is the first time that we visit any node at the level, i.e. the deque for the level does not exist, then we simply create the deque with the current node value as the initial element.
# If the deque for this level exists, then depending on the ordering, we insert the current node value either to the head or to the tail of the queue.
# At the end, we recursively call the function for each of its child nodes.
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []
        def dfs(node, level):
            if level >= len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level+1)

        # normal level order traversal with DFS
        dfs(root, 0)

        return results

# Approach 1 BFS with 2 queue(My soln) and two nested loops 
# Time compelxity O(n)
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root is None:
            return levels
        def isEven(x):
            return x %2 == 0
        next_level = deque([root])
        while next_level:
            # Reverse the list to get correct zigzag order
            next_level.reverse()
            curr_level = next_level
            next_level = deque()
            levels.append([])
            next_level = []
            for node in curr_level:
                levels[-1].append(node.val)
                node_level = len(levels) -1
                if isEven(node_level):
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
        return levels    
