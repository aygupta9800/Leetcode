
#Approach two : Adding powers of two
# Intution:  notice that each time we do a search, we repeatedly go through the same doubles to find the largest. 
# Instead of doing this, we should find a way so that we can compute the sequence just once and then use the results from this to compute our quotient.
#  notice one more property about the difference. That property is that the difference will always be less than the previous doubling of the divisor that fits into it.

#Time complexity : Log(n)
# logn to find the biggest divend, then we just use previously stored results in logn
# O(logn) + o(logn) = O(logn)
#Space : O(Logn)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647 # 2**31 -1
        INT_MIN = -2147483648 # -2**31
        INT_HALF_MIN = -1073741824
        
        #Special case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        #we need to convert both no. to negative as negative range value is
        # bigger and thus no overflow
        # lets count no. of negatives
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        doubles = []
        powersOfTwo = []
        # count quoteint
        quotient = 0
        powerOfTwo = 1
        while dividend - divisor <= 0:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)
            # Prevent needless overflows from occuring...
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor # Double divisor
            powerOfTwo += powerOfTwo
        
        # Go from largest double to smallest, checking if the current double fits into the remainder of the dividend.
        for i in reversed(range(len(doubles))):
            if doubles[i] >=  dividend:
                quotient += powersOfTwo[i]
                dividend -= doubles[i]
            
        return quotient if negatives != 1 else -quotient 
            

# Approach 1 using Exponential Search
# Let n be the absolute value of dividend.

# Time Complexity : O(\log^2 \, n).
# LOG N for finding the biggest number that fits into the current dividend.
# logn for number of times maxm we need to repeat the process
#Space complexity O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647 # 2**31 -1
        INT_MIN = -2147483648 # -2**31
        INT_HALF_MIN = -1073741824
        
        #Special case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        #we need to convert both no. to negative as negative range value is
        # bigger and thus no overflow
        # lets count no. of negatives
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        # count quoteint
        quotient = 0
        while dividend - divisor <= 0:
            powerOfTwo = 1
            value = divisor
            while value >= INT_HALF_MIN and value + value >= dividend:
                value += value
                powerOfTwo += powerOfTwo
            
            
            quotient += powerOfTwo
            dividend -= value
            
        return quotient if negatives != 1 else -quotient 

# Using Bitwise operator:
# NOTE: for negative odd no. n >> 1 is 1 less than our expected value but since our all doubles are even we dont need to cover this edge case.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647 # 2**31 -1
        INT_MIN = -2147483648 # -2**31
        INT_HALF_MIN = -1073741824
        
        #Special case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        #we need to convert both no. to negative as negative range value is
        # bigger and thus no overflow
        # lets count no. of negatives
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        

        # count quoteint
        quotient = 0
        highestDouble = divisor
        highestPow2 = 1
        while highestDouble >= INT_HALF_MIN and dividend <= highestDouble + highestDouble:
            highestPow2 += highestPow2
            highestDouble += highestDouble
            
        quotient = 0
        while dividend <= divisor:
            if dividend <= highestDouble:
                quotient += highestPow2
                dividend -= highestDouble
            
            highestPow2 >>= 1
            highestDouble >>= 1
        
            
        return quotient if negatives != 1 else -quotient 
            

            
