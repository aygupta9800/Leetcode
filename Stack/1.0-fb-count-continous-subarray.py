# You are given an array a of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfills the following conditions:
# The value at index i must be the maximum element in the contiguous subarrays, and
# These contiguous subarrays must either start from or end with i.

# Output
# An array where each index i contains an integer denoting the maximum number of contiguous subarrays of a[i]
# Example:
# a = [3, 4, 1, 6, 2]
# output = [1, 3, 1, 5, 1]

# Explanation:
# For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
# For index 1 - [4], [3, 4], [4, 1]
# For index 2 -[1]
# For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
# For index 4 - [2]
# So, the answer for the above input is [1, 3, 1, 5, 1]


#LOGIC:
# For me the aha moment was realizing that we need to iterate from i...n with some i as the currently left-most max of a subarray.

# You can use a stack..
# Think of it like a train picking up potential maxes as it runs from 0 to N.
# It always picks up every element.
# If the next element is larger, it immediately drops that element off.
# The "dismounted" or dropped-off element travelled a distance of 1. This covers the always-possible single-element sub array.



def count_subarrays(arr):
  # Write your code here
  stack = []
  ways = [0]* len(arr)
  
  for i, n in enumerate(arr):
    while len(stack) != 0 and n > arr[stack[-1]]:
      index = stack.pop()
      ways[index] = i - index
    stack.append(i)
    
  while len(stack) != 0:
    index = stack.pop()
    ways[index] = len(arr) - index
    
  # For left max subarray we can reverse count
  for i in range(len(arr)-1, -1, -1):
    # to not count single subarray two times
    ways[i] -= 1
    while len(stack)!=0 and arr[i] > arr[stack[-1]]:
      index = stack.pop()
      ways[index] = index - i
    stack.append(i)
  
  while len(stack) != 0:
    index = stack.pop()
    ways[index] = index
  return ways


# Solution approach 1
# Letting L[i] be the number of valid subarrays ending at index i and R[i] be the number of valid subarrays beginning at index i, we’ll have output[i] = L[i] + R[i] - 1. Computing R[1..N] is equivalent to computing L[1..N] if a were reversed, allowing us to reduce the problem to computing L[1..N] for an array of N distinct integers.

# Solution approach 2
# We can next observe that the index of the latest element to the left of the ith element which is larger than it determines which subarrays ending at index i are valid - specifically, the ones beginning to the right of that larger element. Letting G[i] be equal to the largest index j such that j < i and a[j] > a[i] (or equal to 0 if there’s no such j), then L[i] = i - G[i]. We’ve now reduced the problem to computing these values G[1..N] for an array of N distinct integers.

# Solution approach 3
# Computing G[i] for each i from 1 to N is a promising approach, but we’ll still need to consider how to do so as efficiently as possible. We can observe that it’s not possible to compute G[i] purely based on the values of G[i-1], a[i-1], and a[i]; we may need more information about earlier a values as well, but would like to avoid simply scanning over all of them. Out of earlier indices j (such that j < i), we can consider which indices are worth considering as potential candidates for G[i] - for example, if there exists a pair of indices j and k such that j < k and a[j] < a[k], can index j ever be a candidate for G[i] for any i > k? If we can maintain information about the set of these possible candidate indices as we go through the array, it’s possible to efficiently determine the one that’s actually equal to G[i] for each i.

