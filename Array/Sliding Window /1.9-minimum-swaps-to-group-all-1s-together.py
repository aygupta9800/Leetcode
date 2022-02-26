# Given a binary array data, return the minimum number of swaps required to
# group all 1’s present in the array together in any place in the array.

# Input: data = [1,0,1,0,1]
# Output: 1
# Explanation: There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1


# To count min swap of 1s, we can count total 1s in array, 
# then we can maintain a window of total1s size and calculate max ones in any such window.
# our swap count will be total ones - max ones in a window
#Time : O(n), space O(1)
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
        data = [1, 0, 1, 0, 1]
        []
        """
        ones = sum(data)
        countOnes = maxCount = 0
        
        l = r = 0
        while r < len(data):
            # updating the no. of 1's by adding new element
            countOnes += data[r]
            # r += 1
            # maintain window len
            if r - l + 1 > ones:
                countOnes -= data[l]
                l += 1
            if r - l + 1 == ones: 
                maxCount = max(maxCount, countOnes)
            r += 1
        return ones- maxCount
        