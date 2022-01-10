#Approach 1 -> traverse and reverse O(m*n)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        i = 0
        j = 0
        m = len(mat)
        n = len(mat[0])
        while 0<=i < m and 0<=j < n:
            while i >= 0 and j <n:
                res.append(mat[i][j])
                if i == 0 or j == n-1:
                    if j < n-1:
                        j += 1
                    else: 
                        i += 1 
                    break
                else:
                    i -= 1
                    j += 1
            while i < m and j >=0:
                res.append(mat[i][j])
                if i == m-1 or j == 0:
                    if i < m-1:
                        i += 1
                    else: 
                        j += 1 
                    break
                else:
                    i += 1
                    j -= 1
        return res
