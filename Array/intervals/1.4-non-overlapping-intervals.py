# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove
# to make the rest of the intervals non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Approach 1 greedy using start point and tracking prevEnd
#  O(nlogn)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        count = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd, end)
        return count

# Approach 2  Greedy using end points.
# we sort by end points , and if 2 interval overlap, we remove 2nd one only everytime.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        # keep track of prevEnd value
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end: #intervals not overlapping
                end = intervals[i][1]
            else:
                count += 1
        return count
            

        
        