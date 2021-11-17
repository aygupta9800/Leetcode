# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Sliding window + hashmap
# TIme complexity O(l1+ (l2-l1)) where l1 is len(s1), l2 =len(s2)
#space O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # creating array of size 26 which will have freq of each word
        s1map = [0] * 26
        s2map = [0] * 26
        for i in range(len(s1)):
            s1map[ord(s1[i])- ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s2)- len(s1)):
            if self.matches(s1map, s2map):
                return True
            s2map[ord(s2[i+ len(s1)])- ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] -= 1
            
        return self.matches(s1map, s2map)
    
    def matches(self, s1map: list, s2map: list) -> bool:
        for i in range(26):
            if s1map[i] != s2map[i]:
                return False
        return True
        