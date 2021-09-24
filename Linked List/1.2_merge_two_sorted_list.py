# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        #head1, head2, start, current
            #head1.value < head2.value: start = head1, current = head1
            head1= head1.next
            head1.value < head2.value:
            current.next = head1, head1++
            else:
            current.next = head2, head++
            till enD: 
            current.next = head1, hea1++
            current.next = head2, hea2++

        """
        #  we can use dummy for avoiding empty edge case
        # dummy =ListNode(), current = dummy and returns dummy.next
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            start = l1
            current = l1
            l1= l1.next
        else:
            start = l2
            current = l2
            l2 = l2.next
        while l1 and l2:
            if l1.val <= l2.val:
                # start = l1
                current.next = l1
                current = current.next
                l1= l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next
        # no need to iterate till end if one list finishes
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return start
