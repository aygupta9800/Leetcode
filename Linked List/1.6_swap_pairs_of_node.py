# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem
#  without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            #save the pointer
            nextPair = curr.next.next
            second = curr.next
            
            #reverse the pair
            second.next = curr
            curr.next = nextPair
                # as second variable will come before curr now after reverse
            prev.next = second
            
            #update the pointer
            prev = curr
            curr = nextPair
        return dummy.next
                
        
        
        
        