# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Example 3:
# Input: nums = [3,0,3, 1,0,4]
# Output: True
# Explanation: u can reach last from i=2 and from i=0 to i=2

#Approach2: Using Greedy O(n) time, O(n) space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        we only need leftmostGoodIndex, to know if current index is Good or not. so we can just store that when iterating from right to left
        """
        n = len(nums)
        leftmostGoodIndex = n-1
        for i in range(n-2, -1, -1):
            # here nums[i] represent max jump so less is possible
            furthestJump = i+ nums[i]
            if furthestJump >= leftmostGoodIndex:
                leftmostGoodIndex = i
        return leftmostGoodIndex == 0

#Approach1: Using Dp
#O(n2)time, O(n) space
class Solution:
    """
    From a given position, when we try to see if we can jump to a GOOD position.
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            # here nums[i] represent max jump so less is possible
            furthestJump = min(i+ nums[i], n -1)
            dp[i] = any(dp[j] == True for j in range(i+1, furthestJump + 1))
            # for j in range(i+1, furthestJump +1):
            #     if dp[j] == True:
            #         dp[i] = True
            #         break
        return dp[0]
        
        