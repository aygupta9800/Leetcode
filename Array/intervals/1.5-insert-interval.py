# 57. Insert Interval

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

#Approach1: Greedy
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        intervals:
        [[1,2], [3, 8], [6,7], [8, 10], [12, 16]]
        [4, 8]
        """
        output = []
        i, n = 0, len(intervals)
        
        while i < n and newInterval[0] > intervals[i][0]:
            output.append(intervals[i])
            i += 1
            
        # add new interval or merge it
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], newInterval[1])
            
        while i < n:
            interval = intervals[i]
            start , end = interval[0], interval[1]
            i += 1
            # if no overlap:
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
        
