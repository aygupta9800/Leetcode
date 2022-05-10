# Time: nlogn
# its similar to find non-overlapping intervals problem.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # similar to non-overlapping intervals
        if not points:
            return 0
        
        count = 1
        points.sort()
        prevEnd = points[0][1]
        for start, end in points[1:]:
            if start >prevEnd:
                count += 1
                prevEnd = end
            elif start <= prevEnd:
                prevEnd = min(prevEnd, end)
        return count
                
        
        