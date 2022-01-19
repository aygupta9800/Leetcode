# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total //2
        
        if len(A) > len(B):
            B, A = A, B
        n1, n2 = len(A), len(B)
        if len(A) == 0:
            return B[n2//2] if n2 %2 else (B[n2//2 -1] + B[n2//2])/2
        l, r = 0, len(A) -1
        while True:# No need for l <= r as it will not reach end point we know
            i = (l + r) // 2
            j = half - (i+1) -1
            Aleft =  A[i] if i >= 0 else float("-inf")
            Aright =  A[i+1] if i < n1 -1 else float("inf")
            Bleft =  B[j] if j >= 0 else float("-inf")
            Bright =  B[j+1] if j < n2 -1 else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
                if total%2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) /2
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
            
        
            
        

# Naive soln O(m+n)
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         l1, l2 = len(nums1), len(nums2)
#         merge_nums = [0]*(l1 + l2)
#         i = 0
#         x, y = 0,0
#         while x < l1 and y < l2:
#             if nums1[x] <= nums2[y]:
#                 merge_nums[i] = nums1[x]
#                 x += 1
#             else:
#                 merge_nums[i] = nums2[y]
#                 y+=1
#             i += 1
        
#         while x < l1:
#             merge_nums[i] = nums1[x]
#             x += 1
#             i+=1
#         while y < l2:
#             merge_nums[i] = nums2[y]
#             y +=1
#             i +=1
#         print(merge_nums)
#         if (l1 + l2) % 2 != 0:
#             return merge_nums[(l1+l2)// 2]
#         else:
#             return (merge_nums[(l1 +l2)//2 -1] + merge_nums[(l1+l2)//2])/2