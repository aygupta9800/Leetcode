""" Follow up:
1. What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
2. What if the matrix is so large that you can only load up a partial row into the memory at once?

1. I think we can use Group by category using hashmap to solve this with grouping by r-c
2. same 
"""

# Approach 2: Group by category:
# Since we know same diagonal element will have r-c difference same
# This leads to the following idea: remember the value of that diagonal as groups[r-c].
#  If we see a mismatch, the matrix is not Toeplitz; otherwise it is.
# Time Complexity: O(M*N)
# Space Complexity: O(M+N)
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True


# Approach 1: Compare with top left neighbour:
# TIme: O(m*n)
# Space O(m+n)
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         m , n = len(matrix), len(matrix[0])
#         for r, row in enumerate(matrix):
#             for c, val in enumerate(row):
#                 if r!= 0 and c != 0 and matrix[r-1][c-1] != val:
#                     return False     
#         return True
            