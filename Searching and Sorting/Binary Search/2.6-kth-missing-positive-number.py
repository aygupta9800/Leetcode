# 1539. Kth Missing Positive Number #EAsys
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Find the kth positive integer that is missing from this array.

# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...].
# The 5th missing positive integer is 9.

# Approach 2: Binary search O(logn)
"""
The number of positive integers which are missing before the arr[idx]
 is equal to arr[idx] - idx - 1.
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            # Otherwise, go left.
            else:
                right = mid - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k

#Approach1:O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # if the kth missing is less than arr[0]
        if k <= arr[0] - 1:
            return k
        k -= arr[0] - 1

        # search kth missing between the array numbers
        for i in range(len(arr) - 1):
            # missing between arr[i] and arr[i + 1]
            curr_missing = arr[i + 1] - arr[i] - 1
            # if the kth missing is between
            # arr[i] and arr[i + 1] -> return it
            if k <= curr_missing:
                return arr[i] + k
            # otherwise, proceed further
            k -= curr_missing

        # if the missing number if greater than arr[-1]
        return arr[-1] + k
