# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Given an integer array nums and an integer k,
# return true if it is possible to divide this array into
# k non-empty subsets whose sums are all equal.

#backtracking soln
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalsum = sum(nums)
        if totalsum % k != 0:
            return False
        nums.sort(reverse=True)
        target = totalsum / k
        n = len(nums)
        #keep track of used elem in cur subset so we dont use them
        # again in next subset
        used = [False] * n
        
        def backtrack(first,k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                # if we found one subset, we again have to 
                # start search from beginning in whatever elm not used
                return backtrack(0, k-1, 0)
            
            # if subsetSum > target:
            #     return False
            
            for i in range(first, n):
                if used[i] or (subsetSum + nums[i] > target):
                    continue
                used[i] = True
                if backtrack(i+1, k, subsetSum + nums[i]):
                    return True
                used[i] = False
            return False
        
        # for 4 equal subset, we just need to find 3, 4rth will be 
        #automatically equal
        return backtrack(0, k-1, 0)
                
                
        