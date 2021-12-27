# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        if dif of len >= 2 return false
        lets s be shorter one
        if both the characters not equal than possiblities
         if both are of equal len : remaiing i+1 to end of both same 
         if t one more in len: t[i+1:] == s[i :]
        return False
        """
        ns, nt = len(s), len(t)
        if ns > nt:
            return self.isOneEditDistance(t,s)

        if nt - ns > 1:
            return False
        
        for i in range(ns):
            if s[i]!= t[i]:
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        return nt == ns +1