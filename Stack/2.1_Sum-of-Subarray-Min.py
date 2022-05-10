# We can denote by result[i] the sum of min values of those subarrays (ending with i-th element).
# A=[3,1,2,5,4]
# [3]
# [3,1], [1]
# [3,1,2], [1,2], [2]
# Q. Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
# [3,1,2,5], [1,2,5], [2,5], [5]
# [3,1,2,5,4], [1,2,5,4], [2,5,4], [5,4], [4]
# pattern: such that A[j] <=A[i] and j < i and first min element from left to i.
# result[i] = result[j] + A[i]*(i-j)

# Solution
# This forms the basis of the solution: we build monotonously incressing (well, strictly speaking - non-decreasing) stack. And then find previous less or equal value and reuse it's sum:

# (trick: we add zeros to A and stack to avoid dealing with empty stack)

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)



#Brute force appraoches
# O(n2)
# def sumSubarrayMins(self, arr: List[int]) -> int:
#         s = 0
#         for i in range(len(arr)):
#             start = end = i
#             m = arr[start]
#             while end < len(arr):
#                 m = min(m, arr[end])
#                 s += m
#                 end += 1
#         return s % (10**9 + 7)
        
#Brute force O(n3)
# s = 0
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)+1):
#         s += min(arr[i: j])
# return s