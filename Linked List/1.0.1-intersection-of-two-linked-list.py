#O(n+m) time, O(1) space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else PB.next
        
        return pA
     # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.