# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#Approach 3: Using quick select algo
# Time complexity : O(N) in the average case, {O}(N^2) in the worst case.
# N+ N/2 +N/4 ... = 2(N)= O(N) avg case. worst case n+n-1+n-2..= O(n^2)
# Space complexity : O(1).
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quick select algorithm
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right]= nums[right], nums[pivot_index]
            
            # 2. move all smaller elements to the left
            p = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # 3. move pivot to its final place
            nums[right], nums[p]= nums[p], nums[right]
            
            return p
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            # If the list contains only one element,
            if left == right:
                return nums[left]
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)
            # find the pivot position in a sorted list
            pivot_index = partition(left,right, pivot_index)
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
             # go left
            elif k_smallest <pivot_index:
                return select(left, pivot_index -1, k_smallest)
             # go right
            else:
                return select(pivot_index + 1, right, k_smallest)
        
        # kth largest is (n - k)th smallest 
        return select(0, len(nums) -1, len(nums) -k)
        
        # """
        # using heap built-in func
        # Time complexity = N.logk =O(nlogk)
        # space complexity: O(1)
        # """
        # return heapq.nlargest(k,nums)[-1]

# Approach2 O(nlogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

# Approach 1 Time complexity O(Nlog(k)) spaceO(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

        