# Approach 2 Using simple array so that u can iterate seq and dont need to repeat 
#loop every time
class Solution:
    def intToRoman(self, num: int) -> str:
        digitMap = [(1000, "M"), (900, "CM"),(500, "D"), (400, "CD"), \
                     (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),\
                     (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        '''
        loop in reverse order such that biggest no. comes first. calculate count and 
        num remain if that symbol is used
        '''    
        res = []
        
        for val, symbol in digitMap:
            if num == 0:
                break

            if num >= val:
                count = num // val #Its crucial for ex 3 is III
                num = num % val
                res.append(symbol*count)
        return "".join(res)
        

# Approach 1 Using hashmap
class Solution:
    def intToRoman(self, num: int) -> str:
        hash_table = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        
        '''
        if its 4 print IV, IX, XL, XC, CD, CM
        Check if its in dic returns that number
        Loop through the dict and find the maxm value it can take
        divide the number, add the roman to string and continue for remaining number
        till there is no remainder
        '''    
        # x = num
        res = ""
        while num:
            mx = None
            for t in hash_table:
                if t > num:
                    break
                mx = t
            if mx:
                num = num - mx
                res += hash_table[mx]
        return res
        