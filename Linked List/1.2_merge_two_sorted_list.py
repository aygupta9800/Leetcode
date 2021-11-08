# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity : O(n + m)O(n+m)

# Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs
# for a number of iterations equal to the sum of the lengths of the two lists. All other work is constant, so the overall complexity is linear.

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

# Approach 2: with recursion
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
