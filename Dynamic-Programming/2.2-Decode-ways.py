#Approach2 : without using extra space
"""
from dp soln we can see we only need one and 2 back values to
calculate current value
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        #no leading zeroes
        if s[0] == '0':
            return 0
        n = len(s)
        two_back = 1 #empty string can be encode 1 way
        one_back = 1 #1 char can be encoded 1 way
        
        for i in range(1, n):
            curr = 0
            if s[i]!="0":
                curr = one_back
            ch = int(s[i-1:i+1])
            if ch in range(10, 27):
                curr += (two_back if i-2 >=0 else 1)
            two_back = one_back
            one_back = curr
        return one_back


# Code 1 Dp with O(n) time O(n) space
class Solution:
    def numDecodings(self, s: str) -> int:
        #no leading zeroes
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0 for i in range(n)]
        # base condn, for string[0] no.of ways to encode = 1
        dp[0] = 1
        
        for i in range(1, n):
            # Check if successful single digit decode is possible
            if s[i]!="0":
                dp[i]= dp[i-1]
            # Check if successful two digit decode is possible.
            # if last 2 char forms valid no.
            ch = int(s[i-1:i+1])
            if ch in range(10, 27):
                # no. of ways to encode empty string is 1
                dp[i] += (dp[i-2] if i-2 >=0 else 1)
            # whether current 0 can be valid encode ch has to be 10 or 20.
            # 00, 30, 40 are invalid ch
            #we can avoid writing this too ex. 130
            # as neither dp[i-1] or dp[i-2] will be added so it will remain default 0
            # elif s[i] == "0": 
            #     return 0  
        return dp[n-1]
        