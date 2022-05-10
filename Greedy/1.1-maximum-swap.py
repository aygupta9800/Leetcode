# 670. Maximum Swap
# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:
# Input: num = 9973
# Output: 9973
# Explanation: No swap.

class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Explanation
        Basic idea:
        Find a index i, where there is a increasing order
        On the right side of i, find the max value (max_val) and its index (max_idx)
        On the left side of i, find the most left value and its index (left_idx), which is less than max_val
        Swap above left_idx and max_idx if necessary
        """
        s = list(str(num))
        n = len(s)
        for i in range(n-1):  # find index where s[i] < s[i+1], meaning a chance to flip
            if s[i] < s[i+1]: break
        else:
            return num
        max_idx, max_val = i +1, s[i+1]
        for j in range(i+1, n):
            if s[j] >= max_val:
                max_idx, max_val = j, s[j]
        left_idx = i
        for j in range(0, i+1):
            if s[j] < max_val:
                left_idx = j
                break
        # print(i, left_idx)
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]
        return int(''.join(s))
            