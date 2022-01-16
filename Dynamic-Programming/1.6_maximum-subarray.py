#Approach2 - Using Dynamic programming - kadanes'algorithm
"""
any subarray whose sum is positive is worth keeping.
Let's start with an empty array, and iterate through the input,
adding numbers to our array as we go along. 
Whenever the sum of the array is negative, we know the entire array
is not worth keeping, so we'll reset it back to an empty array.

"""
# O(n) time
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_sum = best_sum = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        
        return best_sum

# If we have to find subarray as well(kadane algo)
def max_subarray(numbers):
    """Find a contiguous subarray with the largest sum."""
    best_sum = 0  # or: float('-inf')
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

    return best_sum, best_start, best_end

#Appraoch 1 # Using prefix sum
# O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        i = 1
        min_sum = min(0, nums[0])
        curr_sum = nums[0]
        while i < len(nums):
            curr_sum += nums[i]
            # print("c", curr_sum, ",", min_sum)
            res = max(res, curr_sum - min_sum)
            min_sum = min(curr_sum, min_sum)
            i += 1
        return res

#Approach3 #Using dynamic programming 
# TIme: O(nlogn)
"""
If we were to split our input in half, then logically the optimal subarray either:
Uses elements only from the left side
Uses elements only from the right side
Uses a combination of elements from both the left and right side
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)
