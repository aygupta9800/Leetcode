# Intuition

# The nodes in the list are already linked, and hence the rotation basically means
# 1. To close the linked list into the ring.
# 2. To break the ring after the new tail and just in front of the new head.

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        length = 1
        cur = head
        # calculate total len
        while cur.next:
            length += 1
            cur = cur.next
        # CLose the ring
        cur.next = head
        
        k = k%length
        cur = head
        # we have to go n-k-1 pos node where we will break the ring
        for i in range(length - k -1):
            cur = cur.next
        newHead = cur.next
        
        # break the ring
        cur.next = None
        
        return newHead