
# Given a string s, find the length of the longest 
# substring without repeating characters.
# sliding window technique
#Approach 1 code:
def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charIndexMap = {}
        left = 0
        for i in range(len(s)):
            if s[i] in charIndexMap and charIndexMap[s[i]] >= left:
                left = charIndexMap[s[i]] + 1
            res = max(res, i-left+1)
            charIndexMap[s[i]] = i
        
        return res

#My soln
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic ={}
        start = end = 0
        max_len = 0
        
        while end < len(s):
            if s[end] in dic and dic[s[end]] >= start:
                start = dic[s[end]] + 1
            dic[s[end]] = end
            
            # print(end, start)
            max_len = max(max_len, end- start + 1)
            end += 1
        
        return max_len

#  use 2 pointers i and start(correct optimised soln )
# def lengthOfLongestSubstring(self, s: str) -> int:
#     dic = {}
#     max_length = start = 0
#     for i in range(len(s)):
# #       if last visited same char is after the current start
# #       as the length will be less than prev max length we increase start to next to last visited
# # ***** VERY IMP: start <= dic[s[i]]
#         if s[i] in dic and start <= dic[s[i]]:
#             start = dic[s[i]] + 1
#         else:
#             max_length = max(max_length, i - start + 1)
#         # add last visted index for current value
#         dic[s[i]] = i
#     return max_length
