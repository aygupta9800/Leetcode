#Appraoch2 - odd, even case dp[i] = dp[i//2]+ i%2
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] *(n+1)
        for i in range(1, n+1):
            #right shift by 1 bit is same as dividing by two
            dp[i] = dp[i >> 1]+ i% 2
        return dp


#Approach1 dp[i] = dp[i- offset], offset is power of 2 variable
"""
0 - 0000
1 - 0001 dp[i] = 1+ dp[i- most_significantbitval] = 1+ dp[i-1]
2 - 0010 1+ dp[i-2]
3 - 0011 1+ dp[i-2] 
4 - 0100 1+ dp[i-4]
5 - 0101 1+ dp[i-4]
6 - 0110 1+ dp[i-4]
7 - 0111 1+ dp[i-4]
8 - 1000 1+ dp[i-8]
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1+ dp[i-offset]
        return dp
        