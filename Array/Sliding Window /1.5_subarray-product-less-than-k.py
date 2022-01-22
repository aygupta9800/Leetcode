# Given an array of integers nums and an integer k, return the number of contiguous
# subarrays where the product of all the elements in the subarray is strictly less than k.

# Example 1:

# Input: nums = [10,5,2,6], k = 100 
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0

# Approach 1 sliding window
# ex 10 5 2 k = 100
    # 10- > prod = 10, ans = r-l+1 = 1 i.e [10]
    # 10, 5 -> 2 prod = 50, ans += 2 i.e [5], [10,5]
    # 10, 5, 2 -> product > k
    # 5, 2  ->  ans += 2 i.e[5,2], [2]
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            # counting subarray formed with right pointers as end from left elem
            ans += right - left + 1
        return ans
        