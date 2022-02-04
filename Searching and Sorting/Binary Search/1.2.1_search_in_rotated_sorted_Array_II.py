# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.
# With duplicate elem allowed in array
# nums =[1,0,1,1,1] target =0
# output: True
# time complexity: O(n) worst when all are duplicate , O(logn) when all distinct
# space O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def existsInFirst(nums, left, elem):
            return nums[left] <= elem
        def isBinarySearchHelpful(nums, left, elem):
            return nums[left] != elem
        if len(nums) == 0: return False
        l, r = 0, len(nums) -1
        while l <= r:
            mid = (l +r)// 2
            if nums[mid] == target:
                return True
            if not isBinarySearchHelpful(nums, l, nums[mid]):
                l += 1
                continue
            midInFirst = existsInFirst(nums, l, nums[mid])
            targetInFirst = existsInFirst(nums, l, target)
            # If mid and target exist in different sorted arrays,  xor is true when both operands are distinct
            if midInFirst ^ targetInFirst:
                if midInFirst:
                    l = mid +1
                else:
                    r = mid -1
            else:
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid -1
        return False

# Approach 2
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N=len(nums)
        start=0
        end=N-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return True
			# add this line to handle duplicate
            while nums[start]==nums[mid] and start<mid:
                start=start+1
            if nums[start]<=nums[mid]:
                if nums[start]<=target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1