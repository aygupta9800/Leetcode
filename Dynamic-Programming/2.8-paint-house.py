# https://leetcode.com/problems/paint-house/

# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
# Return the minimum cost to paint all houses.


# Example 1:
# Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

#Approach2 Optimised 1d array:
# TImeO(n*3), spaceO(n)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        where i is house, j is color
        dp[0] = cost[i][0]+ min(dp[1], dp[2])
        dp[1] = cost[i][1]+ min(dp[0], dp[2])
        dp[2] = cost[i][2]+ min(dp[0], dp[1])
        We cant use this way because we would be altering say dp[0] value which
        will have next row cost. so we need to save in temp variables.
        
        """
        dp = [0, 0, 0]
        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]
            
            
        return min(dp)

# Approach1 using 2d matrix -dp
#O(n*3)time, O(n*3) space
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        where i is house, j is color
        dp[i][0] = cost[i][0]+ min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1]+ min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2]+ min(dp[i-1][0], dp[i-1][1])
        
        """
        dp = [[0] * 3 for i in range(len(costs)+1)]
        for i in range(len(costs)):
            dp[i+1][0] = costs[i][0] + min(dp[i][1], dp[i][2])
            dp[i+1][1] = costs[i][1] + min(dp[i][0], dp[i][2])
            dp[i+1][2] = costs[i][2] + min(dp[i][0], dp[i][1])
            
        return min(dp[len(costs)])