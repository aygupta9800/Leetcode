# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

#Binary search with finding leftmost bound
# TIme: O(log(n-k)+k), Space: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # left bound cant be more than n-k
        left , right = 0, len(arr) -k
        
        # we have to find left most bound
        # so left distance will be less than left +k elem dis
        while left < right:
            mid = (left+right)// 2
            # distance of left point from x < k+1 left point from x
            if x -arr[mid] > arr[mid+k] -x:
                left = mid+1
            else:
                right = mid
        # print("left",left, right,"right")
        return arr[left: left+k]

# Appraoch 2 binary search + sliding window 
# TIme O(logn+k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]

# Time O(nlogn+klogk) spce O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key= lambda num: [abs(x-num), num])
        print(sorted_arr)
        return sorted(sorted_arr[:k])