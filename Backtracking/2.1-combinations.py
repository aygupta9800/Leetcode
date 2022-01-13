# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n+1):
                #Include i the elem in curr
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        
        output = []
        backtrack()
        return output