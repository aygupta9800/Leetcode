#Easy
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Using Boyer-Moore Voting Algorithm
# O(n) time o(1) space 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        increase and decrease the count if curr is not same as assumed majority element
        It returns a candidate which can be majority element. 
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

# using hashmap O(n) time O(n) space complexity
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)
        