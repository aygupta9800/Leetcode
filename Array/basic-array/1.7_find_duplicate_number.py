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
        
        while low < high:
            cur = (low +high) // 2
            count = 0
            
            # Count how many numbers are less than or equal to 'cur'
            # since for and after duplicate element in [1, n], no. of element <= curr_elem will be > elem  in nums we 
            # can reduce our search space acc with binary search
            count = sum(num<=cur for num in nums)
            if count > cur:
                #save elem and then move in left range to see if there is smaller elem
                # duplicate = cur
                high = cur
            else:
                low = cur + 1
        return low
            
# Approach2: negative marking approach
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate

# Approach1 : Using hashset
# Brute force(not uses constant extra space so not valid with constraint)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numset = set()
        for i, n in enumerate(nums):
            if n in numset:
                return n
            numset.add(n)