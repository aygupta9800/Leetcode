# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# You may assume the input array always has a valid answer.

 

# Example 1:

# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
# Example 2:

# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]

# BRuteforce Nlogn time O(n) space
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        bruteforce O(nlogn), o(n) space
        sort, keep pointer in end, and keep 1 copy of array and start i = 1
        in that
        keep placing elements with i+2 increase till i<n
        then do i = 0, and fill remaing j to 0 elem in orginal array to copy 
        with i+2 increase
        sorted order = a b c d e f
        res=           c f b  e a d
    
        """
        nums.sort()
        arr = nums.copy()
        n = len(nums)
        j = n -1
        # placing biggest elements in middle
        i = 1
        while i <n:
            arr[i] = nums[j]
            i+= 2
            j -= 1
        i =0 
        while i <n:
            arr[i] = nums[j]
            i += 2
            j -= 1
        
        for i in range(n):
            nums[i] = arr[i]
        
            