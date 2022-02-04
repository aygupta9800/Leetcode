# https://leetcode.com/problems/regular-expression-matching/
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".


# Approach 2: Bottom up DP
# TIme : O(n*m), space(O(n*m)) => n string len, p pattern len
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Bottom up variation:
        dp = [[False] * (len(p)+1) for _ in range(len(s) + 1)]
        # when both are out of bound
        dp[-1][-1] = True
        
        for i in range(len(s), -1, -1):
            #dp[len(s)][len(p)] is already calculated
            for j in range(len(p) -1, -1, -1): 
                firstMatch = i<len(s) and  p[j] in (s[i], ".")
                if j+1 < len(p) and p[j+1] == "*":
                    # use * or not use *
                    dp[i][j] = dp[i][j+2] or firstMatch and dp[i+1][j]
                else:
                    dp[i][j] = firstMatch and dp[i+1][j+1]
        return dp[0][0]

# Approach 1: Top down DP using recursion
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top down memoization
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            # if both are out of bound then they match
            if i>= len(s) and j >= len(p):
                return True
            # if only pattern out of bound then they dont match
            if j >= len(p):
                return False
            
            firstMatch = i<len(s) and  (s[i] == p[j] or p[j] ==".")
            # does following char is *  
            if (j+1)< len(p) and p[j+1] == "*":
                # dont use *
                cache[(i, j)] = (dfs(i, j+2) or # dont use *
                    (firstMatch and dfs(i+1, j))) # use *
                return cache[(i, j)]
               
            # if no star
            if firstMatch:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]
            
            # if no star and they dont match
            cache[(i, j)] = False
            return cache[(i, j)]
        
        return dfs(0, 0)