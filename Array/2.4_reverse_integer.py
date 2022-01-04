"""
# rev * 10 + rem
# for positive number for outcome to be overflow
either rev > intmax //10 or if rev == intmax// 10 then rem > 7
similar for negative values
"""


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647  #2**31 -1
        INT_MIN = -2147483648 #-2**31
        
        if x == INT_MIN: return 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        
        rev = 0
        while x != 0:
            rem = x %10
            x = x//10 
            if rev > INT_MAX // 10 or (rev == INT_MAX //10 and rem > 7):
                print(rev)
                return 0
            # if rev < INT_MIN // 10 or (rev == INT_MAX //10 and rem < -8):
            #     return 0
            rev = rev * 10 +  rem
        if sign == -1:
            rev = -rev
        return rev