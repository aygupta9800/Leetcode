
#Approach2 - Sliding window with deque, another way to code:
# Time complexity : O(N), since each element is processed exactly twice - it's index added
# and then removed from the deque.

# Space complexity : O(N), since O(N−k+1) is used for an output array and O(k) for a deque.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Algorithm: 
        we keep a deque, and always keeping only greater value than current right elem. In queue we keep index rather than value so to know the boundaries.
        we keep sliding our window by one position, and appending first value of deque in the process. if our q[0] goes out of bound in comparision to left
        than we pop it
        we keep a check whether current window is atleast k size or not, then only we append to result and increase our left pointer
        """
        output = []
        q = deque()
        l, r = 0, 0
        
        # Updating que before inserting cur right elem
        def remove_smaller_elem(r):
            # last elem will be the smallest
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # we append indexes rather than values so that we know q[0] boundary validity
            q.append(r)
            
        # Adding first k-1 values
        while r +1 < k:
            remove_smaller_elem(r)
            r += 1
        # Updating/slding window
        while r < len(nums):
            # removing all the smaller elem from q than the current value
            remove_smaller_elem(r)
            
            # current window boundary check
            if l> q[0]:
                q.popleft()
            
            output.append(nums[q[0]])
            l += 1
            r += 1
        return output
            

# Approach1 Sliding window with deque
# Time complexity : O(N), since each element is processed exactly twice - it's index added
# and then removed from the deque.

# Space complexity : O(N), since O(N−k+1) is used for an output array and O(k) for a deque.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Algorithm: 
        we keep a deque, and always keeping only greater value than current right elem. In queue we keep index rather than value so to know the boundaries.
        we keep sliding our window by one position, and appending first value of deque in the process. if our q[0] goes out of bound in comparision to left
        than we pop it
        we keep a check whether current window is atleast k size or not, then only we append to result and increase our left pointer
        """
        output = []
        q = deque()
        l, r = 0, 0
        # Increasing our right boundaries
        while r < len(nums):
            # removing all the smaller elem from q than the current value
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # current window boundary check
            if l> q[0]:
                q.popleft()
            
            # if current window is of size k(Initially it will be of less size)
            if r+ 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
            