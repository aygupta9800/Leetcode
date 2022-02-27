# We will send a signal from a given node k. Return the time it takes
# for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.

# Example
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

from collections import defaultdict
import heapq

# Time complexity: O(E*logE) => O(E*logV2)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # make adj list
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v, w))
        
        minHeap = [(0, k)] #cost, node
        visit = set()
        t = 0 # total times
        while minHeap and len(visit) < n:
            w1, node = heapq.heappop(minHeap)
            # not needed apparently if block
            if node in visit:
                continue
            visit.add(node)
            t = max(t, w1)

            for nei, neiWei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (w1+ neiWei, nei))
        return t if len(visit) == n else -1









        

