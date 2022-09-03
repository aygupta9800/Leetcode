# 1567. Maximum Length of Subarray With Positive Product

# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
# Return the maximum length of a subarray with positive product.
 
# Example 1:
# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.

# Example 2:
# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

# Example 3:
# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].


# Approach 2 Dynamic programming but with using only last position variable
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        """
        we need to know the curr positive and curr negative value to determine what will be next curpos and curr nega
        and max of all curr pos is max pos
        
        we just need last value and not all
        """
        pos = 0
        neg = 0
        maxpos = 0
        for i, n in enumerate(nums):
            if n > 0:
                pos = pos + 1
                neg = neg + 1 if neg > 0 else 0
            elif n < 0:
                # we need to avoid reassigning by using temp so
                # or we can use swap thing in python
                neg, pos = pos + 1, neg +1 if neg > 0 else 0
            # number is zero than no neg and pos sub array with it possible
            
            else:
                neg = 0
                pos = 0
            maxpos = max(maxpos, pos)
        return maxpos
        
# Approach 1 Using DP Not optimised for space
def getMaxLen(self, nums: List[int]) -> int:
	n = len(nums)
	pos, neg = [0] * n, [0] * n
	if nums[0] > 0: pos[0] = 1
	if nums[0] < 0: neg[0] = 1
	ans = pos[0]
	for i in range(1, n):
		if nums[i] > 0:
			pos[i] = 1 + pos[i - 1]
			neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
		elif nums[i] < 0:
			pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
			neg[i] = 1 + pos[i - 1]
        # no need to put pos and neg = 0 if nums[i] = 0 as its default value
        # else:
        #     pos[i] = 0
        #     neg[i] = 0
		ans = max(ans, pos[i])
	return ans