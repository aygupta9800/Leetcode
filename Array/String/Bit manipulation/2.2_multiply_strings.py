# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

#TIme COmplextiy(O(n*m)) where n and m are len of num1 and num2
#Logic
# pos of nums[i1]*nums[i2] = i1+i2 when multiplied in reverse order. we have to put carry in next pos
#Space O(n+m) for storing n+m digits
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        #Reverse both numbers
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        res = [0] * (len(num1) + len(num2))
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                res[i1+i2] += int(num1[i1]) * int(num2[i2])
                res[i1+i2+1] += (res[i1+i2] // 10)
                res[i1+i2] = res[i1+i2] % 10
        # print(res)
        
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        
        res = map(str, res[beg:])
        res = "".join(res)
        return res
                