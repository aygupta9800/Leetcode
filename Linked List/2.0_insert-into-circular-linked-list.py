# 708. Insert into a Sorted Circular Linked List
# Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
#soln2 # single pass O(n) soln
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        prev, curr = head, head.next
        toInsert = False

        while True:
            
            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break
        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head

# soln 1
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        if head == head.next:
            node = Node(insertVal)
            head.next = node
            node.next = head
            return head
        cur = head
        
        mx, mn = head.val, head.val
        cur = cur.next
        while cur != head:
            mx = max(mx, cur.val)
            mn = min(mn, cur.val)
            cur = cur.next
    
        while 1:
            if cur.val == mx and cur.next.val == mn and (insertVal <= mn or insertVal >= mx):
                node = Node(insertVal)
                node.next = cur.next
                cur.next = node
                return head
            elif cur.val <= insertVal and cur.next.val >= insertVal:
                node = Node(insertVal)
                node.next = cur.next
                cur.next = node
                return head
            else:
                cur = cur.next