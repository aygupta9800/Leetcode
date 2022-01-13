#Botomup appraoch
# Time complexity : O(S*n). On each step the algorithm finds the next F(i)F(i) in nn iterations, where 1\leq i \leq S1≤i≤S. Therefore in total the iterations are S*nS∗n.
# Space complexity : O(S). We use extra space for the memoization table.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        """
        grid(11):
         min (grid(6) +1, grid(9) +1, grid(8)+1)
        """
        # for coin in coins:
        #     for amt in range(coin, amount+1):
        #         dp[amt] = min(dp[amt], dp[amt-coin] +1)
        for a in range(1, amount+1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], dp[a-c] +1)
        return dp[amount] if dp[amount] != float('inf') else -1
       

#Approach1 TOp down recursive soln:
#TIme O(s*n) where S is the amount, n is denomination count.
# Space complexity : O(S)O(S), where SS is the amount to change We use extra space for the memoization table.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [0 for i in range(amount)]
        """
        grid(11):
         min (grid(6) +1, grid(9) +1, grid(8)+1)
         1. Recursive soln
        """
        def coinCount(coins, rem, dp):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if dp[rem-1] != 0:
                return dp[rem - 1]
            min_val = sys.maxsize
            for c in coins:
                res = coinCount(coins, rem-c, dp)
                if (res >= 0 and res < min_val):
                    min_val = 1+ res
                    
            dp[rem -1] = -1 if (min_val == sys.maxsize) else min_val
            return dp[rem -1]
        return coinCount(coins, amount, self.dp)
      
        