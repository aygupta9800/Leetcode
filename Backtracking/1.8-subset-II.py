# Time O(2**n logn)
class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        """
        logic is to not keep duplicate element in next backtrack if it was avoided before as it will generate duplicate results
        """
        
        def backtrack(i, subset):
            if i == len(nums):
            #Copy constructor as we would be changing subsets later 
                res.append(subset[::])
                return 
            
            # All subsets which include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            #ALl subsets which dont include nums[i]
            while i +1  < len(nums) and nums[i]== nums[i+1]:
                i += 1
            backtrack(i+1, subset) 
        
        backtrack(0, [])
        return res
        