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