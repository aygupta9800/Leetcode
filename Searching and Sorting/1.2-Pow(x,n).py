# Approach 1
# Fast Power Algorithm Recursive 
"""
Intution: Assuming we have got the result of x ^ n, how can we get x ^ {2 * n}. using (x^n)^ 2 = x^ 2*n using single computation
if we now x^n we can split into half * half for even, half * half * x for n = odd
"""
#Time complexity: Ologn, space Ologn for recursion stack
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def fastPow(x, n):
            if n == 0:
                return 1.0
            half = fastPow(x, n//2)
            if n %2 == 0:
                return half * half
            else:
                return half * half * x
        
        N = n
        if N <0:
            x = 1/x
            N = -N
        
        return fastPow(x,N)
    
#ITERATIVE Soln:
#Time complexity O(logN)
#Space O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        N = n
        if N <0:
            x = 1/x
            N = -N
            
        # Iterative soln
        i = N
        ans = 1
        """
        Here at each step we multiply are base by its square and divide power by 2
        like 3pow11 becomes 9pow5 and ans = 3 then 81pow3, ans = 3*9, then 
        6561pow1 and ans = 3*9*81 finally ans becomes 3*9*81*6561
        """
        while i > 0:
            if i % 2 == 1:
                ans = ans * x
            x = x * x
            i = i // 2
            
        return ans
        
        
        
        
# Apporach 0 Brute force
  # #Brute force soln:
        # N = n
        # if (N < 0):
        #     x = 1/x
        #     N = -N
        # ans = 1
        # for i in range(0, N):
        #     ans = ans * x
        # return ans