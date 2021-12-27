
#Heap Approach 2
import heapq
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with complexity better than O(n2).
# Time Complexity: let X= min(K, N); X+Klog(X)

# Well the heap construction takes O(X)O(X) time.
# After that, we perform KK iterations and each iteration has two operations. We extract the minimum element from a heap containing XX elements. Then we add a new element to this heap. Both the operations will take O(\log(X))O(log(X)) time.
# Thus, the total time complexity for this algorithm comes down to be O(X + K\log(X))O(X+Klog(X)) where XX is \text{min}(K, N)min(K,N).
# Space Complexity: O(X) which is occupied by the heap.
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # The size of the matrix
        N = len(matrix)
        # Preparing our min-heap
        minHeap = []
        for r in range(min(k, N)): 
            # We add triplets of information for each cell
            minHeap.append((matrix[r][0], r, 0))
        # Heapify our list
        heapq.heapify(minHeap)    
        # Until we find k elements
        while k:
            # Extract-Min
            element, r, c = heapq.heappop(minHeap) 
            # If we have any new elements in the current row, add them
            if c < N - 1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            # Decrement k
            k -= 1
        
        return element  
# Heap approach 1
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        pq = []
        for r in range(rows):
            for c in range(cols):
                pq.append(matrix[r][c])
        res = heapq.nsmallest(k, pq)
        return res[-1]
        