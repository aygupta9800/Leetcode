"""
Median of data stream
middle elem tak ek heap me ho baki dusre heap me ho then 1st max heap and 2nd min heap 
se we can take median if new elements come: first 
"""
# approach1 (Max + min heap)
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1* num)
        
        # make sure every elem in small heap is smaller than large one
        if self.small and self.large and -1* self.small[0] > self.large[0]:
            val = -1* heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # if uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 *heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) +1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1* val)
            

    def findMedian(self) -> float:
        # return result
        if len(self.small) > len(self.large):
            return -1* self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()