# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#Approach 3: without left,right, equal array, Quickselect
class Solution:
    """
    Since order of k element can be anything we can use
    quickselect algo
    """
    
    def dist(self, pt):
        return pt[0] ** 2 + pt[1] ** 2
    
    def find(self, lst, left, right, k):
        if len(lst) == k:
            return [i[0] for i in lst]
        pivot_index = random.randint(left, right)
        pivot = lst[pivot_index][1]
        #Swap pivot with right node:
        lst[right], lst[pivot_index] = lst[pivot_index], lst[right]
        
        p = left
        i = left
        
        while i < right:
            curr = lst[i]
            dist = curr[1]
            if dist < pivot:
                #Swap the ith point with p
                lst[p], lst[i] = lst[i],lst[p]
                p += 1
            i += 1
    
        # Swap p with pivot right elem
        lst[p], lst[right] = lst[right], lst[p]
        len_left = p -left
        if len_left == k:
            return [i[0] for i in lst[left:p]]
        elif len_left >k:
            return self.find(lst, left, p-1, k)
        else:
            return [i[0] for i in lst[left:p]] + self.find(lst,p,right, k-len_left)
            
         
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = [(i, self.dist(i)) for i in points]
        return self.find(lst,0, len(points) -1, k)
    


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

        