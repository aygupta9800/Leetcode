# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Approach 1
"""
find mid, reverse 2nd part and start 2 pointer
comparision from both end of list till right is there.
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        return True
        