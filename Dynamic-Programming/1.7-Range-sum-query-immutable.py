# https://leetcode.com/problems/range-sum-query-immutable/

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Time complexity : O(1)O(1) time per query, O(n)O(n) time pre-computation. Since the cumulative sum is cached, each sumRange query can be calculated in O(1)O(1) time.

# Space complexity : O(n)O(n).
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = [0 for i in range(len(nums)+1)]
        self.dp[0] = 0
        for i in range(0, len(nums)):
            self.dp[i+1] = self.dp[i]+ nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1] - self.dp[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)