# You are given a Perfect Binary Tree where all leaves are on the same level, and every parent has two children.
#  The binary tree has the following definition:

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """
#Approaching 2
# TIme comp O(n) space o(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        # question says Perfect Binary Tree
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root 

#Approach1
import collections

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = collections.deque([root])
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                # node is not the last index at current level
                if i < qlen -1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


        