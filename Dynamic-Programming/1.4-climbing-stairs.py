# https://leetcode.com/problems/climbing-stairs/

#Approach 1 Using dp
# Time complexity : O(n). Single loop upto n.

# Space complexity : O(n). dp array of size n is used.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            # we can reach i-1 and take 1 step or we can reacj i-2 and take 1 step of 2. both of this are disjoint ways
            dp[i] =  dp[i-1]+ dp[i-2]
        return dp[n]

#Appraoch 2 Fibonacci no.
# dp(n) = dp(n-1)+ dp(n-2)
# just need two variables first and second
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2:
        #     return n
        # first = 1
        # second = 2
        # for i in range(3, n+1):
        #     res = first+ second
        #     first = second
        #     second = res
        # return second
        prev = 1 # Dp[0]
        cur = 1 # Dp[1]
        for i in range(2, n+1):
            prev, cur = cur, prev + cur
        
        return cur
