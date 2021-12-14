# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL. solution should use constant memory space. NOT Perfect binary tree***

#Intuition:
# We have to process all the nodes of the tree. So we can't reduce the time complexity any further. However, we can try and reduce the space complexity.
# The reason we need a queue here is because we don't have any idea about the structure of the tree and the kind of branches it has and we need to access all the nodes on a common level, together, and establish connections between them.

# Once we are done establishing the next pointers between the nodes, don't they kind of represent a linked list? 
# After the next connections are established, all the nodes on a particular level actually form a linked list via these next pointers. Based on this idea, we have the following intuition for our space efficient algorithm:
# We only move on to the level N+1 when we are done establishing the next pointers for the level N.
# So, since we have access to all the nodes on a particular level via the next pointers,
# we can use these next pointers to establish the connections for the next level or the level containing their children.
class Solution:
    
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            
            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = childNode
            else:    
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            prev = childNode 
        return prev, leftmost
    
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        
        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost
            
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None
            
            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                
                # Move onto the next node.
                curr = curr.next
                
        return root 

    # Approach 2
    level order traversal o(n) time o(n) space
