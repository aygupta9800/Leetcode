
#Approach1 2 pointers O(n2) time , constant space
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        #odd length
        for i in range(n):
            l, r = i, i
            while l>=0 and r<n and  s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        for i in range(0, n-1):
            l, r = i, i+1
            while l>=0 and r <n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

#Approach2 Using DP o(n2)time O(n) space
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # for len 1
        for i in range(n):
            dp[i][i] = True
            res += 1
        
        # for len 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        # for len 3 and above       
        for start in range(n-3, -1, -1):
            for end in range(start+2, n):
                if s[start] == s[end] and dp[start+1][end-1]:
                    dp[start][end] = True
                    res += 1
        return res
        