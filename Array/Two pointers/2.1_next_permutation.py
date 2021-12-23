# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is impossible, it must rearrange it to the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Time complexity O(n), In worst case, only two scans of the whole array are needed.
#space O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i):
            j = len(nums) -1
            while i <j :
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
    
        i = len(nums) -2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -=1
        if i >= 0:
            j = len(nums) -1
            while nums[j] <= nums[i]:
                j -= 1
            #Swap the first decreaseing elemnt with no. just bigger than it
            nums[i], nums[j] = nums[j], nums[i]
            reverse(nums, i+1)
        else:
            reverse(nums, 0)
                
