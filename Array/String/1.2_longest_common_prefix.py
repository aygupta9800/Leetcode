#Approach2 O(n*m) time n= total strings, m = len of strs[0]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += s[i]
        
        return res

#Approach 1
# find the longest common prefix string amongst an array of strings.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        pref = strs[0]
        plen = len(pref)
        
        for s in strs[1:]:
            while pref != s[0: plen]:
                pref = pref[0: plen -1]
                plen -= 1
                
                if plen == 0:
                    return ""
        return pref
