# Approach 1
# Logic:
# In any sliding window based problem we have two pointers. One right pointer whose job is to expand the current window and then we have the left pointer whose job is to contract a given window. At any point in time only one of these pointers move and the other one remains fixed.

# The solution is pretty intuitive. We keep expanding the window by moving the right pointer. When the window has all the desired characters, we contract (if possible) and save the smallest window till now.

# Time Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings SS and TT. In the worst case we might end up visiting every element of string SS twice, once by left pointer and once by right pointer. |T|∣T∣ represents the length of string TT.

# Space Complexity: O(∣S∣+∣T∣). |S|∣S∣ when the window size is equal to the entire string SS. |T|∣T∣ when TT has all unique characters.



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)
        
        #Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)
        
        #left and right pointer
        l, r = 0, 0
        
        # formed is used to keep track of how many char in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0
        
        # Dictionary which keeps a count of all the unique char in the current window.
        window_counts = {}
        
        # ans tuple of the form (window len, left, right)
        ans = float("inf"), None, None
        
        while r < len(s):
            
            #Add one char from right of the window
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            #if the freq of current window is of desoired  then increase formed
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            # try to contract window when it ceases to be desirable
            while l <= r and formed == required:
                char = s[l]
                # save the smallest window till now
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                # the char at pos l
                window_counts[char] -=1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]
        