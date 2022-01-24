# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if curr.next and curr.val == curr.next.val:
                #move till the end of the duplicates
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            # otherwise move prev
            else:
                prev = curr
                
            #move forward
            curr = curr.next
                
        
        return dummy.next