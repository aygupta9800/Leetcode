# soln2
# There is just one more question to reply - how to move the left pointer to keep only k distinct characters in the string?

# Let's use for this purpose hashmap containing all characters in the sliding window as keys and their rightmost positions as values. At each moment, this hashmap could contain not more than k + 1 elements.
# Time complexity : O(N) in the best case of k distinct characters in the string and 
# O(Nk) in the worst case of N distinct characters in the string.

# Space complexity : O(k) since additional space is used only for a hashmap with at most k + 1 elements.
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
         we can  keep a dict keeping count of all the distinct char in current window
         if the elem is in window
        """
        N = len(s)
        if k == 0: return 0
        l = r = 0
        max_len = 0
        dic = defaultdict()
        
        while r < N:
            dic[s[r]] = r
            if len(dic) > k:
                min_ind = min(dic.values())
                del dic[s[min_ind]]
                l = min_ind +1
            max_len = max(max_len, r -l +1)
            r += 1
        return max_len
                


# soln 1 O(n)
# we are keeping track of distinct elem with formed
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
         we can  keep a dict keeping count of all the distinct char in current window
         if the elem is in window
        """
        formed = 0
        current_window = defaultdict(int)
        l = r = 0
        res  = 0
        if k == 0:
            return 0
        if len(s) < k:
            return len(s)
        
        while r < len(s):
            if s[r] not in current_window:
                current_window[s[r]] += 1
                formed += 1
            else:
                current_window[s[r]] += 1

            if formed <= k:
                res = max(res, r-l+1)
            
            while formed > k:
                current_window[s[l]] -= 1
                if current_window[s[l]] == 0:
                    formed -= 1
                l +=1
            
            r += 1
        return res
