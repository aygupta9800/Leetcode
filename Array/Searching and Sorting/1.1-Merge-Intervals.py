class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            last = res[-1]
            if intervals[i][0] <= last[1]:
                if intervals[i][1] <= last[1]:
                    continue
                else:
                    res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res
            
        