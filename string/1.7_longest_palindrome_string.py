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