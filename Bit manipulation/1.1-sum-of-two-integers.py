# Approach 2: Pure bit manipulation (For python):
#O(1)time and O(1) space
class Solution:
    def getSum(self, x: int, y: int) -> int:
        mask  = 0xFFFFFFFF
        
        while y != 0:
            x,y = (x^y) & mask, ((x&y) << 1) & mask
            
        max_int = 0x7FFFFFFF
        return x if x < max_int else ~(x^mask)

# Approach 1 O(1) time and space
# language independent soln
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if  x < y:
            return self.getSum(b,a)
        sign = 1 if a >0 else -1
        
        if a * b >= 0:
            # both are of same sign, sum x+y
            # x^y is sum of two number without carry
            # x&Y << 1 is carry shifted by 1 left
            while y:
                x, y = x^y, (x&y)<<1
        
        else:
            # difference of x -y
            # x^y is difference of two number without borrow
            # ~x&Y << 1 is borrow shifted by 1 left
            while y:
                x, y = x^y, ((~x) & y) << 1
                
        return x * sign