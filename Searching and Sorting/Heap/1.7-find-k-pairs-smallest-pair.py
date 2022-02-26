class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        q = [[nums1[0]+nums2[0], (0, 0)]]
        res = []
        visit = set()
        visit.add((0, 0))
        """
        complexity klog(k)
        an index pair, say (1, 1) may come from either (0 + 1, 1) or (1, 0 + 1). You don't want to push (1, 1) twice to the heap.
        """
        
        for x in range(min(k, m*n)):
            val, (i, j) = heapq.heappop(q)
            res.append([nums1[i], nums2[j]])
            if i + 1 < m and (i+1, j) not in visit:
                heapq.heappush(q, [nums1[i+1]+ nums2[j], (i+1, j)])
                visit.add((i+1, j))
            if j + 1 < n and (i, j+1) not in visit:
                heapq.heappush(q, [nums1[i]+ nums2[j+1], (i, j+1)])
                visit.add((i, j+1))
        return res
            
            
            
        