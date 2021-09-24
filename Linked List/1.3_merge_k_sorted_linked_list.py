# You are given an array of k linked-lists lists,
#  each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
            return None
#         merge lists 2 at a time till total list remaining is 1
        while len(lists) != 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(self.merge2Lists(l1, l2))
            lists = mergedList
        return lists[0]
                
    
    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1= l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
            l1 = l1.next
            current = current.next
        if l2:
            current.next = l2
            l2 = l2.next
            current = current.next
        return dummy.next
        