# Time complexity : O(N) since all we do here is four walks along the array of length N.
# Space complexity : O(1) since this is a constant space solution.
class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        # Make all negative values as 0
        n = len(A)
        for i in range(n):
            if A[i] < 0:
                A[i] = 0
        # print(A)
        
        # put negative sign corresponding to valid values
        for i in range(n):
            val = abs(A[i])
            if 1<= val<= n:
                if A[val -1] > 0:
                    A[val -1] *= -1
                elif A[val-1] == 0:
                    A[val-1] = -1*(n+1)
        # print(A)
        
        for i in range(1, n+1):
            if A[i-1] >= 0:
                return i
        
        return n+1
                    
        