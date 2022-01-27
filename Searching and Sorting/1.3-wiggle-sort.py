# O(n) soln

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 2 3 4 5 6 7 8 9
        1 3 2 4 6 5 7 9 8
        1 3 2 5 4 6
        
        
        """
        for i in range(len(nums)-1):
            if (i% 2 == 0 and nums[i] > nums[i+1]) or \
            (i%2 == 1 and nums[i] < nums[i+1]):
                #swap i and i +1
                nums[i], nums[i+1] = nums[i+1], nums[i]
        