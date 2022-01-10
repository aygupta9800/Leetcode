#Approach 1: Using simple iteration and hashmap
class Solution:
    def toHex(self, num: int) -> str:
        dic = { 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f" }
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
            
        s = ""
        while num > 0:
            rem = num % 16
            num = num // 16
            if 9 < rem < 16:
                rem = dic[rem]
            else:
                rem = str(rem)
            s =  rem + s
        return s
            
            