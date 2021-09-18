class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                thissum = nums[i] + nums[l] + nums[r]
                if (abs(target- thissum) < abs(target- res)):
                    res = thissum
                if thissum == target:
                    return thissum
                if thissum < target:
                    l += 1
                else:
                    r -=1
        return res 
            