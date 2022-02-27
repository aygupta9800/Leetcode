# Approach 2:
# Always pop most frequent, then if its more than 2 pop 2nd last
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        ccaccbcc
        c : 6, a:1 b: 1
        Kind of a task schedular question. we pick char based on freq
        maxHeap = [(6, c), (1, a), (1, b)]
        """
        maxHeap = []
        for cnt, c in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if cnt != 0:
                heapq.heappush(maxHeap, (cnt, c))
        res = ""
        while maxHeap:
            cnt, c = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1]==res[-2]==c:
                if not maxHeap:
                    break
                cnt2, c2 = heapq.heappop(maxHeap)
                res += c2
                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(maxHeap, (cnt2, c2))
            else:
                cnt += 1
                res += c
            if cnt != 0:
                heapq.heappush(maxHeap, (cnt, c))
        return res        
        

# Approach1 Like reoragnize string taking prev
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        ccaccbcc
        c : 6, a:1 b: 1
        Kind of a task schedular question. we pick char based on freq
        maxHeap = [(6, c), (1, a), (1, b)]
        ccaccbcc [ (2, c)] prev = None
        """
        maxHeap = []
        for cnt, c in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if cnt != 0:
                heapq.heappush(cnt, c)
        prev = None
        res = ""
        while maxHeap:
            cnt , c = heapq.heappop(maxHeap)
            # check if prev value is more or equal than just take one
            if prev and prev[0] <= cnt:
                res += c
                cnt += 1
            elif cnt <= -2:
                res += c* 2
                cnt += 2
            else:
                res += c
                cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            # print(cnt)
            if cnt < 0:
                prev = (cnt, c)
        return res
