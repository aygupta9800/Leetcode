# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#  Reservoir sampling
# https://leetcode.com/problems/linked-list-random-node/discuss/85659/brief-explanation-for-reservoir-sampling
"""
#decide whether to include the element in reservoid
# choose with probabiliyt k / k+i => k = 1 k+ i = count
"""
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        count = 1
        cur = self.head
        chosen_value = 0
        while cur:
            if random.random() < 1 / count:
                chosen_value = cur.val
            cur = cur.next
            count += 1
        return chosen_value
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()