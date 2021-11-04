# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which
# the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Logic
# What we can do is scan through array with two pointers and check if sum is still less than target then move right pointer
# Once we get the sum >= target that means we can have one subarray as a soln so 
# we keep navigating left to check min len in current subarray
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        n = len(nums)
        left = right = 0
        result = sys.maxsize
        running_sum = 0
        
        while right < n:
            running_sum += nums[right]
            while running_sum >= target:
                result = min(result, right-left+1)
                running_sum -= nums[left]
                left += 1
            right += 1
            
        return result
        