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



# Approach 1: 
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        3
        
        1 1
        1 1 2
        1 1 2 4
        
        if A[i-1] <= A[i] => res[i] = res[i-1] + A[i]
        if A[i] < A[i-1]:
            then we find j < i such that A[j] <= A[i]
            then res[i] = res[j] + (j-i) * A[i]
            
            
        so now we need to keep track of min 
        3 1 2 4 0.5
        
        4
        2
        1
        monostack increasing stack is useful here so that we can keep track of last minium value index we saw.
        it helps in identifying ranges between which a value is min.
        """
        
        res = [0] * len(arr)
        stack = []
        #  we need to handle empty check
        
        for i in range(len(arr)):
            # pop all the indexes whoes value is greater than current value
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            # if stack is empty means i is shortest elem
            if len(stack) == 0:
                res[i] = (i+1) * arr[i]
            else:
                j = stack[-1]
                res[i] = res[j] + (i-j) *arr[i]
            # we need to append the current index in the stack
            stack.append(i)
        return sum(res) % (10 **9+ 7)
                


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