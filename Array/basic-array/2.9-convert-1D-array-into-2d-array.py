# Time O(m,n) space: O(1) Output space not included
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        
        res = [[original[r*n+c] for c in range(n)] for r in range(m)]
        return res
        