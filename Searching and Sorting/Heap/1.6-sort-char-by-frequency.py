# APproach 1 using heap
#Time : 
class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the occurence on each character
        cnt = collections.Counter(s)

        # Build max heap
        heap = [(-cnt, char) for char, cnt in cnt.items()]
        heapq.heapify(heap) #O(n)

        # Build string
        res = []
        # O(nlogk) where k are unique char
        while heap:
            cnt, char = heapq.heappop(heap)
            res += [char] * -cnt
        return ''.join(res)
