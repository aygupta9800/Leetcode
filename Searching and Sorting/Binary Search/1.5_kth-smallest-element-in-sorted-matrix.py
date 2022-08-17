#Approach3: Using Binary search
# TIme O(nlogn)=> time: nlog(max-min) space O(1)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        #O(n) operation
        def countLessEqual(mid):
            count = 0
            larger = matrix[n-1][n-1]
            smaller = matrix[0][0]
            r, c = n-1, 0
            
            while r >= 0 and c < n:
                if matrix[r][c] > mid:
                    #smallest value greater than mid
                    larger = min(larger, matrix[r][c])
                    r -=1
                else:
                    # elem is less than or equal to mid
                    smaller = max(smaller, matrix[r][c])
                    count += r+1
                    c += 1
            return count, smaller, larger
        
        l, r = matrix[0][0], matrix[n-1][n-1]
        #O(log(max-min)operation)
        while l < r:
            mid = (l + r) // 2
             
            if count == k:
                return smaller
            elif count < k:
                l= larger
            else:
                r = smaller
        return l

#Heap Approach 2
import heapq
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with complexity better than O(n2).
# Time Complexity: let X= min(K, N); X+Klog(X)

# Well the heap construction takes O(X) time.
# After that, we perform K iterations and each iteration has two operations. We extract the minimum element from a 
# heap containing X elements. Then we add a new element to this heap. Both the operations will take O(log(X)) time.
# Thus, the total time complexity for this algorithm comes down to be sO(X+Klog(X)) where X is min(K,N).
# Space Complexity: O(X) which is occupied by the heap.
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # The size of the matrix
        N = len(matrix)
        # Preparing our min-heap
        minHeap = []
        # O(min(k,n)) time
        for r in range(min(k, N)): 
            # We add triplets of information for each cell
            minHeap.append((matrix[r][0], r, 0))
        # Heapify our list :O(k) at max
        heapq.heapify(minHeap)    
        # Until we find k elements
        # O(k)
        while k:
            # Extract-Min: O(1) operation
            element, r, c = heapq.heappop(minHeap) 
            # If we have any new elements in the current row, add them
            if c < N - 1: #O(log(min(k, n))) operation
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            # Decrement k
            k -= 1
        
        return element  

# Heap approach 1
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        pq = []
        # O(n2)
        for r in range(rows):
            for c in range(cols):
                pq.append(matrix[r][c])
        #O(n2logk)
        res = heapq.nsmallest(k, pq)
        return res[-1]
        