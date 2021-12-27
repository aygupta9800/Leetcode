# Interview Tip: Whenever you're trying to solve an array problem in-place, always consider the possibility of iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot easier.

#Medium 
# Three pointer(Start from behind)
# TIme complexity O(n+m)
# space O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        for k in range(n +m -1, -1, -1):
            if j < 0 or (i >=0 and nums1[i] >= nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -=1     

#Easy
#Approach 1
# start from beginning
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        k =0
        i = j =0
        for k in range(n +m):
            if j >= n or (i< m and nums1_copy[i] <= nums2[j]):
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j +=1     

#Soln 1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        k =0
        i = j =0
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j +=1     
            k += 1
        while i <m:
            nums1[k] = nums1_copy[i]
            i +=1
            k+=1
        while j <n:
            nums1[k] = nums2[j]
            j +=1
            k +=1
