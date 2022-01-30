#Approach3: Optimised sliding window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        window, counterT = defaultdict(int), Counter(p)
        #we will check if how many unique char freq we have and we need
        have, need = 0, len(counterT)
        # count = 0
        res = []
        for i in range(len(p)):
            char = s[i]
            window[char] += 1
            if char in counterT:
                if  window[char] == counterT[char]:
                    have += 1
                elif window[char] == counterT[char] +1:
                    have -= 1
        if have == need:
            # count += 1
            res.append(0)
        for i in range(len(p), len(s)):
            lchar, rchar = s[i-len(p)], s[i]
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
                res.append(i-len(p)+1)
                # count += 1
        # we dont need to return the count, we can just return res
        return res

# Approach 4: Optimised sliding window with array
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # map of charactar to an index in range a-z. 
        s1count = [0] * 26
        s2count = [0] * 26

        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            index2 = ord(s2[i]) - ord('a')
            s1count[index] = s1count[index] + 1
            s2count[index2] = s2count[index2] + 1
            
        # count how many characters matches are initially set by looking at the first len(s1)
        # characters of s1 and s2. 
        matches = 0
        for index in range(26): # transverse each character.
            if s1count[index] == s2count[index]:
                matches = matches + 1
        
        
        # traverse a fixed window in s2, starting from the left
        # adding a character at a time on the right
        # and removing a character on the left
        left = 0
        for right in range(len(s1), len(s2)): # start after initial window sized to len(s1)
            if matches == 26:
                return True
            
            # update indexes for character that was added on right
            index = ord(s2[right]) - ord('a')
            s2count[index] = s2count[index] + 1 # update character for s
            if s1count[index] == s2count[index]:
                # now they are equal
                matches = matches + 1
            elif s1count[index] + 1 == s2count[index]:
                # they were equal, but now they are not equal anymore
                matches = matches - 1
            
            # update indexes for character that was added on left
            index = ord(s2[left]) - ord('a')
            s2count[index] = s2count[index] - 1
            if s1count[index] == s2count[index]:
                matches = matches + 1
            elif s1count[index] - 1 == s2count[index]:
                matches = matches - 1
            
            # update left window
            left = left + 1
            
        return matches == 26

#Approach2:
#Using 2 arrays of 26 length:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output

# Approach1(Using 2 set counter)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        p_count = Counter(p)
        s_count = Counter()
        
        output = []
        #sliding window on the string s
        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                s_count[s[i-np]] -= 1
                if s_count[s[i-np]] == 0:
                    del s_count[s[i-np]]
                # else:
                #     s_count[s[i-np]] -= 1
            if p_count == s_count:
                output.append(i-np+1)
        return output

        ``