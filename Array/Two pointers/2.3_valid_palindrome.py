# Intuition:
# Since the input string contains characters that we need to ignore in our palindromic check, it becomes tedious to figure out the real middle point of our palindromic input.

# Instead of going outwards from the middle, we could just go inwards towards the middle!
#Approach 2 Time complexity O(n), Space O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) -1
        while i < j:
            while i<j and not s[i].isalnum():
                i += 1
            while i <j and not s[j].isalnum():
                j -=1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

#Soln 1 Time complexity O(n), space O(n) for storing filtered list of alnum
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "": return True
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        # s = ''.join(filter(lambda x: x.isalnum(), s))
        # print(s)
        i = 0
        j = len(s) -1
        while i <= j:
            if s[i] != s[j]:
                return False
            i +=1
            j -= 1
        return True
        