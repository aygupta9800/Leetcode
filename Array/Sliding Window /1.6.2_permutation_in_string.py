# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# optimised sliding window with hash map
# Time: Time complexity: O(l1+(l2-l1))
# Space complexity: O(1)O(1). Constant space is used.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window, counterT = defaultdict(int), Counter(s1)
        #we will check if how many unique char freq we have and we need
        have, need = 0, len(counterT)
        count = 0
        for i in range(len(s1)):
            char = s2[i]
            window[char] += 1
            if char in counterT:
                if  window[char] == counterT[char]:
                    have += 1
                elif window[char] == counterT[char] +1:
                    have -= 1
        if have == need:
            count += 1
        for i in range(len(s1), len(s2)):
            lchar, rchar = s2[i-len(s1)], s2[i]
            window[rchar] += 1
            if rchar in counterT and window[rchar] == counterT[rchar]:
                have += 1
            elif rchar in counterT and window[rchar] == counterT[rchar]+1:
                have -= 1
            window[lchar] -= 1
            if lchar in counterT and window[lchar] == counterT[lchar]:
                have += 1
            elif lchar in counterT and window[lchar] == counterT[lchar] -1:
                have -=1
            if have == need:
                count += 1
        # we dont need to return the count, we can just return true if have= need once
        return count
        



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
        