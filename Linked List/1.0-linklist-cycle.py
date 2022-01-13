# Time complexity : O(n)O(n). Let us denote nn as the total number of nodes in the linked list. To analyze its time complexity, we consider the following two cases separately.

# List has no cycle:
# The fast pointer reaches the end first and the run time depends on the list's length, which is O(n)O(n).

# List has a cycle:
# We break down the movement of the slow pointer into two steps, the non-cyclic part and the cyclic part:

# The slow pointer takes "non-cyclic length" steps to enter the cycle. At this point, the fast pointer has already reached the cycle. \text{Number of iterations} = \text{non-cyclic length} = NNumber of iterations=non-cyclic length=N

# Both pointers are now in the cycle. Consider two runners running in a cycle - the fast runner moves 2 steps while the slow runner moves 1 steps at a time. Since the speed difference is 1, it takes \dfrac{\text{distance between the 2 runners}}{\text{difference of speed}} 
#  steps at a time. Since the speed difference is 1, it takes \dfrac{\text{distance between the 2 runners}}{\text{difference of speed}} 
# difference of speed
# distance between the 2 runners
# ​
#   loops for the fast runner to catch up with the slow runner. As the distance is at most "\text{cyclic length K}cyclic length K" and the speed difference is 1, we conclude that
# \text{Number of iterations} = \text{almost}Number of iterations=almost "\text{cyclic length K}cyclic length K".

# Therefore, the worst case time complexity is O(N+K)O(N+K), which is O(n)O(n).

# Space complexity : O(1)O(1). We only use two nodes (slow and fast) so the space complexity is O(1)O(1).




# Approach 2: Floyd's Cycle Finding Algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True

# Approach 1
# BRute force using hashset
# TIme : O(n)
#  We visit each of the nn elements in the list at most once. Adding a node to the hash table costs only O(1)O(1) time.
# space: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False