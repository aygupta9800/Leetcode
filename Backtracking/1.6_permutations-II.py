# A key insight to avoid generating any redundant permutation is that at each step
# rather than viewing each number as a candidate, we consider each unique number as the true candidate.
# For instance, at the very beginning, given in the input of [1, 1, 2], we have only two true candidates instead of three.

# Algorithm
# Given the above insight, in order to find out all the unique numbers at each stage, we can build a hash table (denoted as counter), with each unique number as the key and its occurrence as the corresponding value.

# TIme Complexity: O(∑k=1toN P(N,k))
# Upper bound : N. N! since N steps of single comb and N! total comb if no overlapping effort

# Space Complexity: O(N)

# First of all, we build a hash table out of the input numbers. In the worst case where each number is unique, we would need O(N) space for the table.

# Since we applied recursion in the algorithm which consumes some extra space in the function call stack, we would need another O(N) space for the recursion.

# During the exploration, we keep a candidate of permutation along the way, which takes yet another O(N).

# To sum up, the total space complexity would be O(N)+O(N)+O(N)=O(N).

# Note, we did not take into account the space needed to hold the results. Otherwise, the space complexity would become O(N⋅N!).

class Solution:
    """
    logic here is to avoid multiple same level branch from duplicate elem
    we can use counter map, so we can choose duplicate value in next level only if left
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make deep copy of resulting permutation 
                # since we need to backtrack later
                results.append(comb[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    #add to comb
                    comb.append(num)
                    counter[num] -= 1
                    #continue exploration
                    backtrack(comb, counter)
                    #revert the choice for next exploration
                    comb.pop()
                    counter[num] += 1
                
            
        backtrack([], Counter(nums))
        return results
                
        