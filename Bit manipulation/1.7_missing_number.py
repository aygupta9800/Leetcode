# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# Approach3 : Using simple Math
# time:O(n), space: O(1)
from json import tool


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        sum of 0 +1+.. n = (n*n+1) // 2
        """
        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Approach Negative indexing
class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        zeroFlag = False
        n = len(nums)
#         Scan for all zeroes and change it to len +1
        for i, x in enumerate(nums):
            if x == 0:
                zeroFlag = True
                nums[i] = n+1
        if not zeroFlag:
            return 0
        # do negative indexing
        for i,x in enumerate(nums):
            x = abs(x)
            if x <= n:
                nums[x-1] = -1* nums[x-1]
        # return non negative index
        for i, x in enumerate(nums):
            if x > 0:
                return i+1
            

# Approach2 Using bit manipulation
# xor index with value and len(n) too
# result will be 0 xor missing number i.e missing number
# missing =4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
# =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
# =0∧0∧0∧0∧2
# =2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i^num
        return missing
    
    

#Approach2 Using hash set 
# Time O(n), space: O(n)
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

# Approach 1 Using binary search
# Time O(nlogn) space O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        missing = -1
        while low <= high:
            mid = (low + high) // 2
            count = 0
            count += sum(1 for i in nums if i <= mid)
            # print(count, "==", mid, "low", low, "high", high)
            if count == mid+1:
                low = mid +1
            else:
                missing = mid
                high = mid -1
        return missing