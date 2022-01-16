class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[i] represents the length of the longest increasing subsequence
        that ends with the ith element. 
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+ dp[j])
        
        return max(dp)
        