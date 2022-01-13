#APproach2 Backtracking with dynamic programming
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        dp = [[False] * n for _ in range(n)]
        
        for end in range(0, n):
            for start in range(0, n):
                dp[start][end] = s[start] == s[end] and (end-start < 2 or dp[start +1] [end -1])
                
        def backtrack(first, comb, dp):
            #base condn
            if first == len(s):
                res.append(comb[::])
                return
            # here i represend end of the substring
            for end in range(first, len(s)):
                if dp[first][end]:
                    # dp[first][end] = True
                    comb.append(s[first: end+1])
                    backtrack(end+1,comb, dp )
                    comb.pop()
        
        backtrack(0, [], dp)
        return res
        

#Approach 1 make palindrom string starting from index first
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s):
            return s == s[::-1]
        def backtrack(first, comb):
            #base condn
            if first == len(s):
                res.append(comb[::])
                return
            # here i represents end of the substring
            for i in range(first+1, len(s)+1):
                if not isPalindrome(s[first:i]):
                    continue
                comb.append(s[first: i])
                backtrack(i, comb)
                comb.pop()
        
        backtrack(0, [])
        return res
        