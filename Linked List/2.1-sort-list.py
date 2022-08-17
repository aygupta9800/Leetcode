# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



#Approach2 Using Bottom up constant space, nlogn time soln
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Bottom up iterative
        """
        if not head or not head.next: return head
        dummy = ListNode('s'); dummy.next = head; tmp = head
        length = 0
        while tmp:
            tmp = tmp.next
            length += 1
        step = 1
        while step<length:
            cur, tail = dummy.next, dummy
            while cur:
                left = cur
                right = self.split(left,step)
                cur = self.split(right, step)
                tail = self.merge2(left,right,tail)
            step <<= 1
        return dummy.next
    
    # merge 2 sorted lists, and append the result to head
    # return the tail
    def merge2(self, p1, p2, tail):
        dummy = ListNode('#'); p = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next; p = p.next
            else:
                p.next = p2
                p2 = p2.next; p = p.next
        p.next = p1 or p2
        tail.next = dummy.next
        while p.next: p = p.next
        return p

    # divide the linked list into two lists
    # first linked list contains n nodes
    # return the head of second linked list
    def split(self, head, n):
        for i in range(n-1): 
            if head: head = head.next
            else: break
        if not head: return None
        second = head.next
        head.next = None
        return second
        

# Approach1 using top down merge sort
# time O(nlogn) - split logn height , o(n) for merge at every level
# Space Complexity: O(logn) , where n is the number of nodes in linked list. Since the problem is recursive, we need additional space to store the recursive call stack. The maximum depth of the recursion tree is \log nlogn

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Top down merge sort
        """
        def getMid(head):
            # not needed as it is checked before calling this function
            # if not head or not head.next:
            #     return head
            fast, slow = head.next, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            mid = slow.next
            slow.next = None
            return mid
        # merge 2 sorted linked list in constant space
        def merge(lst1, lst2):
            dummy = ListNode()
            cur = dummy
            while lst1 is not None and lst2 is not None:
                if lst1.val < lst2.val:
                    cur.next = lst1
                    lst1= lst1.next
                    cur = cur.next
                else:
                    cur.next = lst2
                    lst2= lst2.next
                    cur = cur.next
            cur.next =  lst1 if lst1 != None else lst2
            return dummy.next
            
        if head == None or head.next == None:
            return head
        
        mid = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
        