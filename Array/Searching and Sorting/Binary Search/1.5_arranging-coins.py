# 441. Arranging Coins
# Easy

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            k = (l+ r) // 2
            curr = k * (k+1) //2
            if curr == n:
                return k
            if curr < n:
                l = k+1
            else:
                r = k-1
        return r
        