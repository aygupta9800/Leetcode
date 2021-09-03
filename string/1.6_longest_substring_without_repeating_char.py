# sliding window technique
def lengthOfLongestSubstring(self, s: str) -> int:
    dic = {}
    max_length = start = 0
    for i in range(len(s)):
#         if last visited same char is after the current start
        if s[i] in dic and start <= dic[s[i]]:
            start = dic[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        dic[s[i]] = i
    return max_length