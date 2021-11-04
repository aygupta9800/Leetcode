#  Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string
# and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get 
# after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

#Logic: At a given time, string can be replaced if total str len - max char length i.e replace lenght is <= k
# if not we move window start with 1 position

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = end = 0
        dic = defaultdict(lambda: 0)
        max_len = 0
        dic[s[end]] = 1
        while end < len(s):
            #char_to_replace
            repLen = (end -start + 1) - max(dic.values())
            # print("==rep",repLen)
            if repLen > k:
                dic[s[start]] -= 1
                start += 1
            else:
                max_len = max(max_len, end -start + 1)
                end += 1
                if end < len(s):
                    dic[s[end]] += 1
        
        return max_len
        