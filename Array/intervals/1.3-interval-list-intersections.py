# 986. Interval List Intersections
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.


# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Intuition

# In an interval [a, b], call b the "endpoint".
# Among the given intervals, consider the interval A[0] with the smallest endpoint. (Without loss of generality, this interval occurs in array A.)
# Then, among the intervals in array B, A[0] can only intersect one such interval in array B. (If two intervals in B intersect A[0], then they both share the endpoint of A[0] -- but intervals in B are disjoint, which is a contradiction.)
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        
        while i < len(A) and j < len(B):
            
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            
            # is intersection
            if low <= high:
                ans.append([low, high])
            
            # Discard the smallest endpoint interval
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans
        