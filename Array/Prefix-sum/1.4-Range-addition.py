# Approach 1
# O(n+u) where n is lenth and u is len of updates.
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        just mark st and end +1 boundaries with increment val in updates
        then use prefix sum 
        as we are adding certain value at st ind and removing it after end +1
        we are negating its affect after certain update boundary so prefix sum works
        """
        arr = [0]* length
        for u in updates:
            st, end, inc = u[0], u[1], u[2]
            arr[st] += inc
            if end +1 < length :
                arr[end+1] -= inc
        # Add prefix sum
        cur_sum = 0
        for i, a in enumerate(arr):
            arr[i] += cur_sum
            cur_sum = arr[i]
        return arr