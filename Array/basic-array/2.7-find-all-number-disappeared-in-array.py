# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n]
# that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# approach 2 O(1) Space InPlace Modification Solution
# We will be negating the numbers seen in the array and use the
# sign of each of the numbers for finding our missing numbers.
# We will be treating numbers in the array as indices and mark corresponding
# locations in the array as negative.
# time O(n), space O(1) In-place solution, by negating values
# as we encounter in array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            new_i = abs(nums[i]) -1
            if nums[new_i] > 0:
                nums[new_i] *= -1
        
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
    
        return res

# appraoch1 Using hashset O(N) O(N) time space
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not 
        # really concerned with the frequency of numbers.
        hash_table = set()
        
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table.add(num)
        
        # Response array that would contain the missing numbers
        result = []
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table. 
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
                
        return result    