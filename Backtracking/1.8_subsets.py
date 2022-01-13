
#Approach 2:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        # nums.sort()
        """
        logic is to not keep element or not for current i index in nums
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
            # while i +1  < len(nums) and nums[i]== nums[i+1]:
            #     i += 1
            backtrack(i+1, subset) 
        
        backtrack(0, [])
        return res        

# Time Complexity: O(N.2^N)
# Space complexity: O(N). We are usingO(N) space to maintain curr, and are modifying curr in-place with backtracking. Note that for space complexity analysis, we do not count space that is only used for the purpose of returning output, so the output array is ignored.




# Logic: Given the definition, the problem can also be interpreted as finding the power set from a sequence.
# So, this time let us loop over the length of combination,
#  rather than the candidate numbers, and generate all combinations for a given length with the help of backtracking technique.
#Appraoch 1:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first = 0, curr = []):
            # if the combinations is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into current comb
                curr.append(nums[i])
                #use next integers to complete the combination
                backtrack(i+1, curr)
                #backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return output