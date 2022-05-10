# O(n) time complexity
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        Here we can say Sum(max- min of subarr) 
        = sum(max)of subarr - sum(min)
        so if we find prevsmalles and next smallest elem of current elem
        then we can say all subarray with it wil have current as minimum
        Vicersa for max case
        1 2 3 4 5
        stack as we need a point
        stack = [1,2,4]
        minstack = non decreasing
        maxstack = non increasing stack
        """
        res = 0
        inf = float("inf")
        s = []
        # first finding prev smaller and next smaller using increasing monotonic stack
        A = [-inf]+nums+[-inf]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                # prev smaller index
                k = s[-1]
                # subtracting prevsmallest to current * current * next smallest subarrays for which popped elem is minimum
                res -= A[j]* (i-j)*(j-k)
            s.append(i)
        A = [inf] + nums + [inf]
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                # prev bigger index
                k = s[-1]
                # adding 
                res += A[j] * (i-j)*(j-k)
            s.append(i)
        return res
                
        