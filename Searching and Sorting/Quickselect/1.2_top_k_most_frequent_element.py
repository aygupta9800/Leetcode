
# Top k frequent elements
# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.
 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 
#Approach 4 Quick select Algorithm
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        # print(unique)
        
        def partition(left, right, pivot_index):
            pivot = count[unique[pivot_index]]
            
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            
            p = left
            for i in range(left, right):
                if count[unique[i]] < pivot:
                    unique[p], unique[i] = unique[i], unique[p]
                    p+= 1
            
            unique[right], unique[p] = unique[p], unique[right]
            return p
        
        def quickselect(left, right, k_smallest):
            if left == right:
                return
            
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if pivot_index == k_smallest:
                return
            elif pivot_index > k_smallest:
                quickselect(left, pivot_index -1, k_smallest)
            else:
                quickselect(pivot_index+1, right, k_smallest)
            
        n = len(unique)

        quickselect(0, n-1, n-k)
        return unique[n-k:]

# Bucket sort approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        #O(n)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        #O(n*k)
        for i in range(len(freq) -1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


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