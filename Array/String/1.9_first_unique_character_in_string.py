# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# The idea is to go through the string and save in a hash map the number of times each character appears in the string.
# That would take \mathcal{O}(N)O(N) time, where N is a number of characters in the string.
# And then we go through the string the second time, this time we use the hash map as a reference to check if a character is unique or not.

# My solution O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] = -1
            else:
                dic[s[i]] = i
        for key in dic:
            if dic[key] != -1:
                return dic[key]
        return -1

#Using collections (Leetcode)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1