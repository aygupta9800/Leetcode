# Given a string s, find the length of the longest 
# substring without repeating characters.
# sliding window technique
#  use 2 pointers i and start
def lengthOfLongestSubstring(self, s: str) -> int:
    dic = {}
    max_length = start = 0
    for i in range(len(s)):
#       if last visited same char is after the current start
#       as the length will be less than prev max length we increase start to next to last visited
        if s[i] in dic and start <= dic[s[i]]:
            start = dic[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        # add last visted index for current value
        dic[s[i]] = i
    return max_length