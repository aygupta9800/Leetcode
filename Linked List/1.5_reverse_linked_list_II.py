# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #Empty list
        if not head:
            return None
        
        # move 2 pointer until they reach left point
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left-1, right-1
            
        #The two pointer that will fix final connection
        tail, con = cur, prev
        
        # Iteratively reverse the nodes until n becomes 0
        while right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            right -= 1
        
        #Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        # Tricky: if left is 1
        else:
            head = prev
        
        tail.next = cur
        return head


# Approach 2 Using dummy to avoid edge cases:
# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         dummy = ListNode(0, head)
        
#         # 1) reach node at position "left"
#         leftPrev, cur = dummy, head
#         for i in range(left - 1):
#             leftPrev, cur = cur, cur.next
        
#         # Now cur="left", leftPrev="node before left"
#         # 2) reverse from left to right
#         prev = None
#         for i in range(right - left + 1):
#             tmpNext = cur.next
#             cur.next = prev
#             prev, cur = cur, tmpNext
            
#         # 3) Update pointers
#         leftPrev.next.next = cur # cur is node after "right"
#         leftPrev.next = prev     # prev is "right"
#         return dummy.next
                
        