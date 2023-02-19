class Solution:
    def jump(self, nums: List[int]) -> int:

        """
        We only need leftmost index 
        
        
        """
        
        n = len(nums)
        dp = [float("inf") for i in range(n)]
        
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            furthestJump = min(i +nums[i], n-1)
            for j in range(i+1, furthestJump+1):
                dp[i] = min(dp[i], dp[j] +1)
        return dp[0]


    # solution 2
class Solution:
    def jump(self, nums: List[int]) -> int:

        """
        If we loop from start, we need till when we can go farthest,
        and whenever we reach currentJumpEnd index we need to update our
        jump count by 1 and currentJumpEnd by farthest Index
        """
        jumps = 0
        currentJumpEnd = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentJumpEnd:
                jumps += 1
                currentJumpEnd = farthest
        return jumps
                