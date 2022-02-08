# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Approach2 without reversing input
"""
Algo:
1. calculate len(l1) and len(l2)
2. sum two linked list without taking carry into consideration
    add every new node to front so that we can traverse back
3. start from end and keep adding cary and reversing the list
4. in end if carry is left, append in start as Head
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Sum corresponding positions and build an output by adding to front
        2. Take care about carry, and reverse the output
        # parse both lists
        # and sum the corresponding positions 
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3<-10<-10 --> 4->1->0
        """
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next 
            n1 += 1
        while curr2:
            curr2 = curr2.next 
            n2 += 1
        
        curr1, curr2 = l1, l2
        head = None
        
        while n1 > 0 and n2> 0:
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n2 > n1: # not equal
                val += curr2.val
                curr2 = curr2.next
                n2 -= 1
                
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr           
            
        #take carry in account and reverse
        curr1, head = head, None
        carry = 0
        prev = None
        while curr1:
            sm = curr1.val+carry
            carry, val = sm // 10, sm % 10
            curr1.val = val
            temp = curr1.next
            curr1.next = prev
            prev = curr1
            curr1 = temp
        head = prev
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr
        return head
                
# Approach1
"""
Algorithm:
1. write reverselinklist fn
2. reverse both link list
3. add both link list such that every node in output is added in front
"""