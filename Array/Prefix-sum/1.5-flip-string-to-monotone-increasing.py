# A binary string is monotone increasing if it consists of some number of 0's (possibly none),
#  followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.


# Approach 1 Prefix sum/ Dynamic programming
# Time complexity: O(n), space O(n)
# Example 1:
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

# Example 2:
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        We can use prefix sums. Say P[i+1] = A[0] + A[1] + ... + A[i], where A[i] = 1 if S[i] == '1', else A[i] = 0. We can calculate P in linear time.

Then if we want x zeros followed by N-x ones, there are P[x] ones in the start that must be flipped, plus (N-x) - (P[N] - P[x]) zeros that must be flipped. The last calculation comes from the fact that there are P[N] - P[x] ones in the later segment of length N-x, but we want the number of zeros.
        010110
        010
        
        """
        #calculate prefix sum of 1's for each pos
        P = [0]
        for x in s:
            P.append(P[-1]+int(x))
            
        # for x ans is P[x] + (n-x) -(P[n]-P[x]) ie n
        return min(P[x] + len(s)-x -(P[-1]-P[x]) for x in range(len(P)))
        
        