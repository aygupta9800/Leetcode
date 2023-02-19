# Given a string s, return the longest palindromic substring in s.
# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
#logic: 
# 1. Naive approach: take substring and check if its palindrome by comaparing from ends of substring and reduce size
# 2. optimised approach: if sth is palindrome then from center of it will also we can compare

def longestPalindrome(self, s: str) -> str:
    """
    we check from i as center, longest palindrome and update in our res
    we need to check for odd and even len both
    """
    res = ""
    resLen = 0
    # for every element we iterate and find longest palindrom at which it is at center
    for i in range(len(s)):
        #odd length
        l, r = i ,i
        while l >= 0 and r <len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res= s[l: r+1]
                resLen = r-l+1
            l -= 1
            r += 1 
        # even length
        l, r = i, i +1
        while l >= 0 and r <len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res= s[l: r+1]
                resLen = r-l+1
            l -= 1
            r += 1
    return res

# Approach 2 Dynamic Programming dp[i][j] = dp[i+1][j-1]
#O(n2), spaceO(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = s[0] #every single char is palindrome
        maxLen = 1
        
        # for len 1
        for i in range(n):
            dp[i][i] = True
        # for len 2
        for i in range(n-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1] == True and maxLen == 1:
                res = s[i:i+2]
                maxLen = 2
        # checking with length 3 onwards and start point from end
        # as dp[i][j] depends on dp[i+1][j-1]
        for start in range(n-3, -1, -1):
            for end in range(start +2, n):
                if s[start] == s[end] and dp[start+1][end-1]: 
                    dp[start][end] = True
                    if end - start +1 > maxLen:
                        res = s[start: end+1]
                        maxLen = end-start+1
        return res
                
                  
            
# Approach 3: dp but with looping for window size
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        
        dp = [[False for j in range(n)] for i in range(n)]
        
        # Base condn
        for i in range(n):
            dp[i][i] = True
        
        mxLen = 1 
        res = s[0]
        
        # 2 size window
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True 
                if mxLen < 2:
                    mxLen = 2
                    res = s[i: i+2]
        
        # j = window size, i starting point, i+j-1 end point
        for j in range(3, n+1):
            for i in range(n-j, -1, -1):
                if s[i] == s[i+j -1] and dp[i+1][i+j-2]:
                    dp[i][i+j-1] = True
                    if mxLen < j:
                        mxLen = j
                        res = s[i: i+j]
        
        return res
        
        