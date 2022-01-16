# https://leetcode.com/problems/target-sum/

# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

#  Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1

# Approach 2 Dynamic programming
# IF WE KNOW (sum, i) =  (sum -nums[i], i-1) + (sum + nums[i], i-1)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Dynamic programming
        """
        totalSum = sum(nums)
        if target not in range(-totalSum, totalSum+1): return 0
        dp = [[0 for j in range(totalSum * 2+ 1)] for i in range(len(nums))]
        
        # We took totalSum as offset as sum will always be [-totalsum, totalSum] range and this would make our some positive
        
        #Base case
        dp[0][totalSum + nums[0]] += 1
        dp[0][totalSum - nums[0]] += 1
        
        # i is index, j is sum till that pos
        for i in range(1, len(nums)):
            for j in range(0, 2* totalSum +1):
                if j-nums[i] >= 0:
                    dp[i][j] += dp[i-1][j- nums[i]]
                if j + nums[i] <= totalSum * 2:
                    dp[i][j] += dp[i-1][j + nums[i]]
        return dp[-1][target + totalSum]
                
        



# Appraoch1 using recursion with memoization
# Time complexity: O(t⋅n). The memo array of size O(t⋅n) has been filled just once. Here, tt refers to the sum of the numsnums array and n refers to the length of the nums array.

# Space complexity: O(t⋅n). The depth of recursion tree can go up to n. The memo array contains t⋅n elements.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Recursion with memoization
        we can se multiple subproblem getting repeated for (i, total)
        """
        dp = {} #(index, total) -> # of ways
        
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = backtrack(i+1, total + nums[i]) + \
            backtrack(i+1, total - nums[i])
            return dp[(i, total)]
        
        return backtrack(0, 0)