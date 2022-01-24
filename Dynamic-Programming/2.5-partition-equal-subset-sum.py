"""
We maintain a 2D array , dp[n][subSetSum] For an array element ii and sum j in array nums,

dp}[i][j] = true}dp[i][j]=true if the sum jj can be formed by array elements in subset nums[0]} .. nums[i]}nums[0]..nums[i],otherwise dp}[i][j] = false}dp[i][j]=false

dp}[i][j]dp[i][j] is true}true it satisfies one of the following conditions :

Case 1) sum j can be formed without including ith element,
if dp[i−1][j]==true

Case 2) sum j can be formed including ith element,
if dp[i−1][j−nums[i]]==true
"""
#Approach 2 Using DP, 2d table
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        if totalsum %2 != 0: return False
        
        target = totalsum // 2
        n = len(nums)
        
        # construct db table of n+1 * subsetsum + 1
        dp = [[False]* (target+1) for _ in range(n+1)]
        # sum 0 can be formed without including any index
        dp[0][0] = True
        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(target+1):
                if j < curr:
                    dp[i][j]= dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
        return dp[n][target]
                

#Approach3 Using dp 1D array:
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]

#Approach 2 using DP Time: O(sum*n)=O(m*n), space:O(sum)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        if totalsum %2 != 0: return False
        
        target = totalsum // 2
        n = len(nums)
        dp = set()
        # here dp keeps subsetsum possible from end 
        dp.add(0)
        for i in range(n-1, -1, -1):
            nextDP = dp.copy()
            # as we cant traverse and add in set at same time
            for t in dp:
                nextDP.add(t+nums[i])
            dp= nextDP
        return True if target in dp else False
                
 

#Approach 1 Using backtracking with memoization
# O(m*n) entries in hash
class Solution: 
    def canPartition(self, nums: List[int]) -> bool:
        """
        totalSum should be even
        backtrack(first, target, sum1, sum2):
        for any i
            backtrack(first+1, target, sum1+first, sum2)
             or backtrack(first+1, target, sum1, sum2+first)
        """
        @lru_cache(maxsize=None)
        def backtrack(nums, n, subset_sum):
            if subset_sum == 0:
                return True
            if n ==0 or subset_sum < 0:
                return False
            result = (backtrack(nums, n-1, subset_sum-nums[n-1]) or backtrack(nums, n-1, subset_sum) )
            return result
        totalsum = sum(nums)
        if totalsum %2 != 0: return False
        
        subset_sum = totalsum // 2
        n = len(nums)
        return backtrack(tuple(nums), n-1, subset_sum)