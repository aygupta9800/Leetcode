# given an array of integers nums sorted in ascending order, find the starting and
#  ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# instead of using a linear-scan approach to find the boundaries once the target has been found, 
# let's use two binary searches to find the first and last position of the target.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findBound(nums, target, True)
        last = self.findBound(nums, target, False)
        return [first, last]
      
    
    def findBound(self, nums, target, isFirst):
        N = len(nums)
        l, r = 0, N -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if isFirst:
                    # This means we found our lower bound.
                    if mid == l or target != nums[mid -1]:
                        return mid
                    # Search on the left side for the bound.
                    r = mid -1
                else:
                    # This means we found our upper bound.
                    if mid == r or nums[mid] != nums[mid + 1]:
                        return mid
                    # Search on the right side for the bound.
                    l = mid +1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


# My solution (Naive)
# Binary search + 2 linear scan. Avg time com O(logn) worst O(n)
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         l, r = 0, len(nums) -1
#         index = -1
#         while l <= r:
#             mid = (l+r) //2
#             if nums[mid] == target:
#                 index = mid
#                 break;
#             if nums[mid] > target:
#                 r = mid -1
#             else:
#                 l = mid + 1
#         # print("index", index)
#         if index == -1:
#             return [-1, -1]
#         li, ri = index, index
#         while li > 0 and nums[li] == nums[li -1]:
#             li -= 1
#         while ri < len(nums) -1 and nums[ri] == nums[ri +1]:
#             ri += 1 
#         return [li, ri]
