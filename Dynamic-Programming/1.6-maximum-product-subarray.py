
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Time: O(N), space O(1)
class Solution:
    """
    Instead of just tracking curr_sum which is +ve, we keep track
    of curr_max_prod and curr_min_prod as both can make next products
    max depending on the sign of next numbers ex. -2 * -4 = 8
    """
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        curr_max = nums[0]
        curr_min = nums[0]
        result = curr_max
        
        for i in range(1, n):
            temp_max = max(nums[i], nums[i]*curr_max, nums[i]* curr_min)
            curr_min = min(nums[i], nums[i]*curr_max, nums[i]* curr_min)
            curr_max = temp_max
            result = max(result, curr_max)
            
        return result