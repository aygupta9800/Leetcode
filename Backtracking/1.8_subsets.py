# Time Complexity: O(N.2^N)
# Space complexity: O(N). We are usingO(N) space to maintain curr, and are modifying curr in-place with backtracking. Note that for space complexity analysis, we do not count space that is only used for the purpose of returning output, so the output array is ignored.

# Logic: Given the definition, the problem can also be interpreted as finding the power set from a sequence.
# So, this time let us loop over the length of combination, rather than the candidate numbers, and generate all combinations for a given length with the help of backtracking technique.

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