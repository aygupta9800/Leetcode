# Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValidPalindrome(s, i ,j):
            if i > j:
                return False
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i,j = 0, len(s) -1
        while i<j:
            if s[i] != s[j]:
                return isValidPalindrome(s, i+1, j) or isValidPalindrome(s, i, j-1)
            i += 1
            j -= 1
        return True