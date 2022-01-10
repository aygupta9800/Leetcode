

#Approach 3 Bit manipulation
# The bin() function returns the binary version of a specified integer.
# The result will always start with the prefix 0b.
# Algorithm

# Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.

# While carry is nonzero: y != 0:
    # Current answer without carry is XOR of x and y: answer = x^y.
    # Current carry is left-shifted AND of x and y: carry = (x & y) << 1.
    # Job is done, prepare the next loop: x = answer, y = carry.

# Return x in the binary form.

class Solution:
    def addBinary(self, a, b) -> str:
        # Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.
        x, y = int(a, 2), int(b, 2)
        while y:
            #Here XOR is a key as well, because it's a sum of two binaries without taking carry into account.
            answer = x ^ y
            # To find current carry is quite easy as well, it's AND of two input numbers,
            # shifted one bit to the left.
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

#Approach 2 Bit by Bit computation
# TIme complexity O(n+m)
# space o(n+m)
# using simple logic
"""
1+ 1 = 0, carry = 0
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            
            total = digitA +digitB + carry
            carry = total//2
            total = total %2
            res = str(total)+res
    
        if carry:
            res = "1"+ res
        return res
        
        

# Using Builtin Fn
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2)+ int(b,2))