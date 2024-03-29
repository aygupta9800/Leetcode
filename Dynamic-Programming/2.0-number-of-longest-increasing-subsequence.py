"""
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
"""

# Intuition
# To find the frequency of the longest increasing sequence, we need
# First, know how long is the longest increasing sequence
# Second, count the frequency

# solution 2 starting from end and cal LIS starting at i:
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        LIS[i] representing length of LIS starting at index i
        cnt[i] represent the cnt of LIS starting at i
        
        LIS[i] = LIS[j]+ 1 if nums[j] > nums[i] 
        """
        if not nums:
            return 0
        n = len(nums)
        LIS = [1] * n
        cnt = [1] * n
        mx = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    if LIS[j] + 1 > LIS[i]:
                        LIS[i] = LIS[j]+1
                        cnt[i] = cnt[j]
                    elif LIS[j] +1 == LIS[i]:
                        cnt[i] += cnt[j]
            mx = max(mx, LIS[i])
        mxCount = 0
        for ln, count in zip(LIS, cnt):
            if ln == mx:
                mxCount += count
        return mxCount

"""
# Thus, we create 2 lists with length n
# dp[i]: meaning length of longest increasing sequence
# cnt[i]: meaning frequency of longest increasing sequence

If dp[i] < dp[j] + 1 meaning we found a longer sequence and dp[i] need to be updated, then cnt[i] need to be updated to cnt[j]
If dp[i] == dp[j] + 1 meaning dp[j] + 1 is one way to reach longest increasing sequence to i, so simple increment by cnt[j] like this cnt[i] = cnt[i] + cnt[j]
Finally, sum up cnt of all longest increase sequence will be the solution

"""
# This is a pretty standard DP question. Just like most sequence type of DP question, we need to loop over each element and check all previous stored information to update current.
# Time complexity is O(n*n)
# Implementation
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        m = 1 #longest length
        dp = [1] * n # LIS ending at that pos
        cnt = [1] * n #cnt of longest length sequence till ith position
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1:
                        dp[i], cnt[i] = dp[j]+1, cnt[j]
                    elif dp[i] == dp[j]+1:
                        cnt[i] += cnt[j]
            m = max(m, dp[i])                        
        return sum(c for l, c in zip(dp, cnt) if l == m)
