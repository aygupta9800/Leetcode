# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            # temp = curr
            # curr = curr.next
            # temp.next = prev
            # prev = temp
        return prev


#approach2 recursive In java
# public ListNode reverseList(ListNode head) {
#     if (head == null || head.next == null) return head;
#     ListNode p = reverseList(head.next);
#     head.next.next = head;
#     head.next = null;
#     return p;
# }
