class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        """
        since sequence 
        """
        for a in range(target+1):
            for c in nums:
                if a >= c:
                    dp[a] += dp[a-c]
        
        return dp[a]
        