
# O(n) time complexity
#Approach1
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        1 4 2 3 3
        
        1
        This question can be divided into 
        sum of subarray max - sum of subarray min
        so we keep two monotonic stack, one of max, one for min
        
        
        """
        n = len(nums)
        resMin = [0] * n
        minstack = []
        
        # to handle empty check
        
        for i in range(n):
            while minstack and nums[minstack[-1]] > nums[i]:
                minstack.pop()
            # if stack is empty means i is shortest elem
            if len(minstack) == 0:
                resMin[i] = (i+1) * nums[i]
            else:
                j = minstack[-1]
                resMin[i] = resMin[j] + (i-j) *nums[i]
            # we need to append the current index in the stack
            minstack.append(i)
        # return sum(res) % (10 **9+ 7)
        

        # Now solve for sum of max subarrays
        resMax = [0] * n
        maxstack = []
        
        for i in range(n):
            #pop all the elem which are smaller than current value
            while maxstack and nums[maxstack[-1]] < nums[i]:
                maxstack.pop()
            if maxstack:
                j = maxstack[-1]
                resMax[i] = resMax[j] +(i-j) * nums[i]
            else:
                resMax[i] = (i+1) * nums[i]
            maxstack.append(i)
        
        return sum(resMax) - sum(resMin)
     
        


# Approach 2
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
                
        