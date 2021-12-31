# Reorder list is combination of 3 problems
# 1. find middle elem of list
# 2. reverse of 2nd part of list
# 3. merge two sorted list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Time Complexity: O(N)
# space O(1)
class Solution:
   
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        # find the middle elem.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the 2nd part of list
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        #merge two sorted list
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        