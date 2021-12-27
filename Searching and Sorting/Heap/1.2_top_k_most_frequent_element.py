
# Top k frequent elements
# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.
 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 
#appraoch3 Heap
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key= count.get)


# approach 1 (My solution)O(nlogn)
# using counter
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        for i in nums:
            dic[i] += 1
        ls= list(dic.keys())
        ls.sort(key=lambda x:dic[x] )
        return ls[-k:]
# ====
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(lambda: 0)
        for i in nums:
            dic[i] += 1
        ls= list(dic.keys())
        ls.sort(key=lambda x:dic[x] )
        return ls[-k:]