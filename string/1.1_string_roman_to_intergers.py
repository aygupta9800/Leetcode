# Roman to integer
class Solution:
    #solution 2 optimised youtube
     def romanToInt(self, s: str) -> int:
        # Start by looking from behine. ex "XVIV"
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        N = len(s)
        i = N-1
        while i >= 0:
            if i < N -1 and dic[s[i]] < dic[s[i+ 1]]:
                result -= dic[s[i]]
                i -=1
            else:
                result += dic[s[i]]
                i -=1
        return result
    # solution 1(self solution)
    # def romanToInt(self, s: str) -> int:
    #     i = 0
    #     dic = {
    #         "I": 1,
    #         "V": 5,
    #         "X": 10,
    #         "L": 50,
    #         "C": 100,
    #         "D": 500,
    #         "M": 1000
    #     }
    #     result = 0
    #     while i <  len(s):
    #         if i!= len(s) -1 and dic[s[i]] < dic[s[i+ 1]]:
    #             result += dic[s[i+1]] -dic[s[i]]
    #             i += 2
    #         else:
    #             result += dic[s[i]]
    #             i += 1
    #     return result