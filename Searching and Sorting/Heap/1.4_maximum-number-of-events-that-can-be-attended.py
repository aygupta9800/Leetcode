# Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.
# Return the maximum number of events you can attend.

# Complexity
# Time O(d + nlogn), where D is the range of A[i][1]
# Space O(N)
# from collections import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        #First sort with starting day and then ending day
        events.sort(key = lambda x: (x[0], x[1]))
        pq = []
        count = 0
        #curent day
        d = 0
        i, n = 0, len(events)
        while i< n or pq:
            if not pq:
                d = events[i][0]
            while i<n and events[i][0] == d:
                # push all events we can possibly attend
                heapq.heappush(pq, events[i][1])
                i += 1
            # attend this one event
            heapq.heappop(pq)
            count += 1
            d += 1
            # remove all impossible-to-attend events
            while pq and pq[0] < d:
                heapq.heappop(pq)
        return count
            
                
                