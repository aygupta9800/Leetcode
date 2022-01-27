#Approach1 Binary search from no. 0 to x.
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0,  x
        while l <= r:
            mid = (l+r)// 2
            sqr = mid*mid
            if sqr == x:
                return mid
            elif sqr > x:
                r= mid -1
            else:
                l = mid+1
        return r
        