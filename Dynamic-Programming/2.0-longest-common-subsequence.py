# https://leetcode.com/problems/longest-common-subsequence/

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

#Approach1 Dp
# Time O(n), space: O(1)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        ebade  abcde
        now common sequence can be written in order
        ans = 0
        ans += max([bade, abcde], [ebade, bcde])
        [bade, abcde] += max([bade, bcde], [ade, abcde])
        [ebade, bcde] += max([ebade, cde], [bade, bcde])
        [bade, bcde] = 1+ [ade, cde]
        
        from above we can say
        dp[i][j] = max(dp[i+1][j], dp[i][j+1]) if s1[i] !=s[j]
        dp[i][j] = 1+ dp[i+1][j+1] if s1[i] ==s[j]
        Now base cond
        in end, dp[n][j] = 0 for every j, dp[i][n] = 0 for every i
        """
        n1, n2 = len(text1), len(text2)
        dp = [[0]*(n2+1) for i in range(n1+1)]
        #base case already covered
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if text1[i] ==text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1] 
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]