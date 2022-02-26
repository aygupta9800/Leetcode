
# Approach 1
#time O(n^k-1), for 4 sum O(n3)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        [1, 0, -1, 0, -2, 2], target = 0
        [-2, -1, 0, 0, 1, 2]
        Implement k-2 loops using recursion
        with k = 2 we call 2 sum
        """
        def kSum(nums, target, k):
            res = []
            # if we run out of numbers to add
            if not nums:
                return res
            
            avgval = target//k
            if avgval <nums[0] or avgval>nums[-1]:
                return res
            
            if k == 2:
                return twoSum(nums, target)
            
            # picking a position from array
            for i in range(len(nums)):
                if i==0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]]+subset)
            return res
        
        def twoSum(nums, target):
            res = []
            l, r = 0, len(nums) -1
            while (l< r):
                cur_sum = nums[l] + nums[r]
                if cur_sum < target or (l>0 and nums[l] == nums[l-1]):
                    l += 1
                elif cur_sum > target or (r< len(nums)-1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res
        
        nums.sort()
        return kSum(nums, target, 4)
                    
                    
                                    
                        
        
        
        