# Q. Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
#  You may return the combinations in any order.

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(target, comb, first):
            if target == 0:
                #make a deep copy of the current comb
                res.append(list(comb))
                return
            elif target < 0:
                # exceed the scope, stop the exploration
                return
            
            for i in range(first, len(candidates)):
                #add the number to comb
                comb.append(candidates[i])
                # give current number another chance
                backtrack(target-candidates[i], comb, i)
                #backtrack 
                comb.pop()
            
        backtrack(target, [],0)
        return res