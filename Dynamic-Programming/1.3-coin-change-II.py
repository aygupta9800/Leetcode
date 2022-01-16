# https://leetcode.com/problems/coin-change-2/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

#Time complexity: O(n* amount), space: O(n)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        """
        sequence matters so coins cant be repeated
        """
        for c in coins:
            for a in range(amount+1):
                if a >= c:
                    dp[a] += dp[a-c]
            # print(dp)
        return dp[amount]
        