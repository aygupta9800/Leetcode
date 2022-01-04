# 523. Continuous Subarray Sum # Medium
# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

# Example 1:
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

#Approach 1: Prefix sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
      If you get the same remainder again, it means that you've encountered some sum which is a multiple of K.
        """
        # As for 0 sum if we take at -1 pos than even if 0th pos remainder is 0 lenth will be only 0-(-1) = 1 < 2
        dic = {0: -1} #{remainder: oldest ith pos } oldest pos will give max len of such subarray
        curSum = 0
        for i, n in enumerate(nums):
            # print(dic)
            curSum += n
            curSum %= k
            # print(curSum)
            if curSum in dic:
                if i - dic[curSum] > 1:
                    return True
            else:
                dic[curSum] = i
        return False
