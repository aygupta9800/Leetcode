# Given two positive integers n and k.
# A factor of an integer n is defined as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

# logic: The divisors are paired, i.e., if i is a divisor of N, then N / i is a divisor of N, too.
#  That means it's enough to iterate up to sqrt{N}.
# Math, sqrt{N}). As in Approach 2, let's iterate up to \sqrt{N} N,
# and decrease kk by one at each step. If kk drops down to zero during the iterations - the kth divisor is here.
#  Otherwise, the kth divisor is the paired one and could be found as N / divisors[len(divisors) - k].



class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sqrt_n = int(n ** 0.5)
        divisors = []
        # print(f'{n} {k}')
        for x in range(1, sqrt_n +1):
            if n % x == 0:
                divisors.append(x)
                k -= 1
                if k == 0 :
                    return x
        #if complete square we have to skip duplicates
        if (sqrt_n * sqrt_n == n):
            k += 1
            
        if  k <= len(divisors):
            return int (n / divisors[len(divisors) - k])
        return -1

#Brute force
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = [];
        for x in range(1, n//2+1):
            if n % x == 0:
                res.append(x)
                k -= 1
                if k == 0:
                     return x
        
        res.append(n)
        k -= 1;
        if k == 0:
            return n
        return -1
        