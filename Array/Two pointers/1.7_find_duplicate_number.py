#Find Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# NOTE
# You must solve the problem without modifying the array nums and uses only constant extra space.


#Binary search approach
#logic: [1, 2 ...n] . count of elem <= elem will be same as elem until duplicate element is reached. then it will be elem + 1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # low and high represent the range of the target
        low = 1
        high = len(nums) -1
        
        while low <= high:
            cur = (low +high) // 2
            count = 0
            
            # Count how many numbers are less than or equal to 'cur'
            count = sum(num<=cur for num in nums)
            if count > cur:
                #save elem and then move in left range to see if there is smaller elem
                duplicate = cur
                high = cur -1
            else:
                low = cur + 1
        return duplicate
            
            
            
        

# Brute force(not uses constant extra space so not valid with constraint)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numset = set()
        for i, n in enumerate(nums):
            if n in numset:
                return n
            numset.add(n)