# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:

# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:

# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

#Approach2:
"""
In this approach we dont have to explore every bit even if its not 1
"""
# Time: O(1), space O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n-1 # n = n & n-1
            res += 1
        return res


# Approach1 Exploring every bit by shifting number to right
# Time: O(32)= O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            #checking last digit
            # res += n%2 # or u can do n & 0001
            res += n & 1
            n = n >> 1 # right shift the n
        return res