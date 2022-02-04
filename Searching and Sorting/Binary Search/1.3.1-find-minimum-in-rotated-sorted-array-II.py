# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
# You must decrease the overall operation steps as much as possible.
class Solution:
    """
    to be able to work with duplicate as well we compare
    pivot with high element to reduce search space
    [10,1,10,10,10] => then we cant find min with comparing with adj value 
    """
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) -1
        
        while high >low:
            mid = low + (high - low) // 2
            # risk of overflow low+high // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[high]:
                low = mid +1
            elif nums[mid] < nums[high]:
                high = mid
            else: # when equal we cant reduce search space by half
                high -= 1
        return nums[high]
                
        
        