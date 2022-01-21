class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x >0 and x % 10 == 0):
            return False
        x = str(x)
        l,r= 0, len(x) -1
        while l<r:
            if x[l] != x[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

# Another approach

class Solution:
    def reverseUtil(self, x):
        result = 0

        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)
            
        return result
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x >0 and x % 10 == 0):
            return False
        return x == self.reverseUtil(x)