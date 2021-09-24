# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list
#  and return its head.


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we take dummy so that we remain at 1 elem before the del element 
        # when right reaches null
        dummy = ListNode(0, head)
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        # ptr = left.next
        left.next = left.next.next
    # if u return head then when only head is removed in single element list , it will fail
        return dummy.next