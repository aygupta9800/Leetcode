# You are given an array of k linked-lists lists,
#  each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach2: Using min heap 
# Time: O(klogk), space: O(k)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        q = []
        # here node is pointing to head of that respective lth linked list
        for l, node in enumerate(lists):
            if node:
                # adding l too so that we can put ordering for duplicate values.
                q.append([node.val, l, node])
        heapq.heapify(q)
        while q:
            val, l, node = heapq.heappop(q)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(q, [node.val, l, node])
        return dummy.next

# Approach1 by merging 2 link lists at a time
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
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
        