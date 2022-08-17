#Approach 2: Bucket sort
class Solution:
    def frequencySort(self, s: str) -> str:
        # with Bucket sort
        if not s: return s
        
        count = Counter(s)
        max_freq = max(count.values())
        
        # bucket sort by freq
        freq = [[] for i in range(max_freq+1)]
        for c, i in count.items():
            freq[i].append(c)
        
        # build result string
        res = []
        for i in range(len(freq)-1, 0, -1):
            for c in freq[i]:
                res.append(c*i)
        
        return "".join(res)

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
         # since k can be max 256 char ASCII possible values so time complexity O(n)
        while heap:
            cnt, char = heapq.heappop(heap)
            res += [char] * -cnt
        return ''.join(res)
