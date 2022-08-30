# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random



# Approach 1 Two pass solution
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}
        currentNode = head
        while currentNode:
            oldToNew[currentNode] = Node(currentNode.val, None, None)
            currentNode = currentNode.next
        for old, new in oldToNew.items():
            if old != None:
                new.next = oldToNew[old.next]
                new.random = oldToNew[old.random]
        return oldToNew[head]