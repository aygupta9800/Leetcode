# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is impossible, it must rearrange it to the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

#  Algo:
#  1. start from right and find first elem which is less than its next elem and mark it i
#  2. Now we have to replace this with elem in right which is just bigger than this start from right till you find such elem and mark it j
#  3. now jth elem should be at ith. and for number to be just bigger than last,we need to put ith in right part and sort them in increasing way
#  since if swap ith and jth pos, right part will already be sorted in decreasgin
#  we just need to reverse the right part after swapping
#  4. if i < 0 : then we need to reverse whole array
   

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
                
