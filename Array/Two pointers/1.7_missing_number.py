# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        missing = -1
        while low <= high:
            mid = (low + high) // 2
            count = 0
            count += sum(1 for i in nums if i <= mid)
            # print(count, "==", mid, "low", low, "high", high)
            if count == mid+1:
                low = mid +1
            else:
                missing = mid
                high = mid -1
        return missing