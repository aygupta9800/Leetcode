# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
# (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.




# pseudo code:
# mid = left + right //2
# if nums[mid ] == target:
#     return mid
# if nums[mid] >= nums[left]:
#     if target < nums[mid]:
#         if target >= nums[left]:
#             right = mid -1
#         else:
#             left = mid + 1
#     if target > nums[mid]:
#         left = mid+ 1
#     #first portion
# else:
#     #2nd portion
#     if target < nums[mid]:
#         right = mid -1
#     else:
#         if target >= nums[left]:
#             right = mid -1
#         else:
#             left = mid + 1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1
        while l <= r:
            mid = (l + r)// 2
            # if found
            if target == nums[mid]:
                return mid
            
            #left portion array
            if nums[mid] >= nums[l]:
                # two cases where we need to move l index
                if target > nums[mid] or target < nums[l]:
                    l = mid +1
                else:
                     r = mid -1
            #right portion array
            else:
                # two cases where we need to move r index
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid +1
        return -1
    

# My own solution
# logic: find the larget element first then do binary search in one of the part to find target
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) -1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] > nums[left]:
#                 left = mid
#             elif nums[mid] < nums[left]:
#                 right = mid -1
#             else:
#                 if nums[right] > nums[left]:
#                     left = mid +1
#                 else:
#                     left = mid
#                     right = mid -1
                
#         found = -1
#         if target <= nums[left] and target >= nums[0]:
#             l, r = 0, left
#             while (l <= r):
#                 mid = (l+ r) // 2
#                 if nums[mid] < target:
#                     l = mid +1
#                 elif nums[mid] > target:
#                     r = mid -1
#                 else:
#                     found = mid
#                     break;
# #             Search in first part
#         else:
#             l, r = left+ 1, len(nums)-1
#             while (l <= r):
#                 mid = (l+ r) // 2
#                 if nums[mid] < target:
#                     l = mid +1
#                 elif nums[mid] > target:
#                     r = mid -1
#                 else:
#                     found = mid
#                     break;
#         # search in 2nd part
#         return found
            
                
                
        
        
        