# https://leetcode.com/problems/break-a-palindrome/
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        """
        if len(palindrome) == 1:
            return ""
        lst = list(palindrome)
        i, j = 0, len(lst) -1
        # for i in range(len(lst) // 2):
        while i <=j:
            # if non "a" char is middle we cant replace it to a
            if lst[i] != "a" and i!=j:
                lst[i] = "a"
                return "".join(lst)
            i += 1
            j -= 1
        lst[-1] = "b"
        return "".join(lst)