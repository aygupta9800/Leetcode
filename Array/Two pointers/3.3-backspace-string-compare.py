# Approach 1: Using 2 pointers from end
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) -1
        j = len(t) -1
        
        skipS, skipT = 0, 0
        while i >= 0 or j >= 0:
            # Reach next valid char is s
            while i>=0:
                if s[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            
             # Reach next valid char is t
            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            
            #check if both valid char are inbound and equal.
            if (i >= 0 and j <0) or (j>=0 and i<0):
                return False
            
            if i>= 0 and j >=0 and s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        
        return True
            