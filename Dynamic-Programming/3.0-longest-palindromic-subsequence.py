# Approach 1 using dp : top down approach
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        def recursive(l, r):
            if (l,r) in cache:
                return cache[(l,r)]
            if l == r:
                cache[(l,r)] = 1
            elif l > r:
                cache[(l,r)] = 0
            elif s[l] == s[r]:
                cache[(l,r)] = 2 + recursive(l+1, r-1)
            else:
                cache[(l,r)] = max(recursive(l+1, r), recursive(l, r-1))
            return cache[(l,r)]
        
        return recursive(0, len(s) -1)
            