# easy
# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = collections.Counter(s)
        res = 0
        for key in dic:
            res += dic[key] // 2 * 2
            if res % 2 == 0 and dic[key] % 2 == 1:
                res += 1
        
        return res