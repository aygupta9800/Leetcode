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
                    break;
                mx = t
            if mx:
                num = num - mx
                res += hash_table[mx]
        return res
        