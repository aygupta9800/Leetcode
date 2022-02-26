# time complexity O(nlogn), space O(n)
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        1 8 3 5
        min two lena he
        1 3 3 5 8
        dque
        (((1 + 3)*3 + 5) +8
        1, 3 -3
        5- 2
        8 -1
        Every time we need two min to pick and 1 no. to insert such that maintaing sorted order - Min heap
        """
        totalCost = 0
        heap = [stick for stick in sticks]
        heapq.heapify(heap)
        while len(heap) > 1:
            stick1 = heapq.heappop(heap)
            stick2= heapq.heappop(heap)
            totalCost += stick1+stick2
            heapq.heappush(heap, stick1+stick2)
        return totalCost
            
        