# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# Approach3 : Using simple Math
# time:O(n), space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        sum of 0 +1+.. n = (n*n+1) // 2
        """
        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    

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