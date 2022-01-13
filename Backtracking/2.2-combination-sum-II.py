# Approach 2: Using sorting and skipping same values
# Time Complexity: O(2^N)
# Space Complexity: \mathcal{O}(N)O(N)

# We use the variable comb to keep track of the current combination we build, which requires \mathcal{O}(N)O(N) space.

# In addition, we apply recursion in the algorithm, which will incur additional memory consumption in the function call stack. In the worst case, the stack will pile up to \mathcal{O}(N)O(N) space.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(target, comb, first):
            if target == 0:
                #make a deep copy of the current comb
                res.append(list(comb))
                return
            elif target < 0:
                # exceed the scope, stop the exploration
                return
            
            prev = -1
            for i in range(first, len(candidates)):
#                 # num, count = counter[i]
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                backtrack(target-candidates[i], comb, i+1)
                comb.pop()
                prev= candidates[i]

            
        backtrack(target, [],0)
        return res

# Another way to write approach 2 using sorting
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(target, comb, first):
            if target == 0:
                #make a deep copy of the current comb
                res.append(list(comb))
                return
            elif target < 0:
                # exceed the scope, stop the exploration
                return
            if first == len(candidates):
                return
            
            comb.append(candidates[first])
            backtrack(target-candidates[first], comb, first +1)
            comb.pop()
            i = first
            while i +1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(target, comb, i+1)


# Approach 1: Using counter
"""
Logic: We use counter to avoid duplicate combinations
then we iterate in it from first pointer till end to fill a position
to make this iteration we convert counter into list of tuple(num, count)
so once we passed the certain num, we dont again choose it.
"""

# Time Complexity: O(2^N)
# Space Complexity: O(N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(target, comb, first, counter):
            if target == 0:
                #make a deep copy of the current comb
                res.append(list(comb))
                return
            elif target < 0:
                # exceed the scope, stop the exploration
                return
            
            for i in range(first, len(counter)):
                num, count = counter[i]
                
                if count <= 0:
                    continue
                #add the number to comb
                comb.append(num)
                counter[i] = (num, count -1)
                # give current number another chance
                backtrack(target-num, comb, i, counter)
                #backtrack 
                comb.pop()
                counter[i] = (num, count)
                
        
        
        counter = Counter(candidates)
        # convert counter to list(num, count) tuple for iteration
        counter = [(c, counter[c]) for c in counter]
            
        backtrack(target, [],0, counter)
        return res
        