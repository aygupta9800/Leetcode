# Given an array of integers nums and an integer k, 
# return the total number of continuous subarrays whose sum equals to k.


#Approach3
#prefix sum with hashmap 
# TIme O(n), space O(n)
# no sliding window as negative values allowed
# The logic is simple: the current prefix sum is curr_sum, and some elements before the prefix sum was curr_sum - target. All the elements in between sum up to curr_sum - (curr_sum - target) = target.
# The idea behind this approach is as follows: If the cumulative sum up to two indices is the same, the sum of the elements lying in between those indices is zero. Extending the same thought further, if the cumulative sum up to two indices, say ii and jj is at a difference of kk i.e. if sum[i] - sum[j] = k, the sum of elements lying between indices ii and jj is kk.

# Based on these thoughts, we make use of a hashmap mapmap which is used to store the cumulative sum up to all the indices possible along with the number of times the same sum occurs. We store the data in the form: (sum_i, no. of occurrences of sum_i). We traverse over the array numsnums and keep on finding the cumulative sum. Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. Further, for every sum encountered, we also determine the number of times the sum sum-ksum−k has occurred already, since it will determine the number of times a subarray with sum kk has occurred up to the current index. We increment the countcount by the same amount.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        # {sum: no. of occurences of sum}
        prefixSums = {0: 1}
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            # since we are having 0: 1 before ,means we are taking case of all the elements from start so we need to add curr index to prefix hashmap after count is increase.
            prefixSums[curSum]= 1 +prefixSums.get(curSum, 0)
        return res

#Another way to write same logic
from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        count = curr_sum = 0
        h = defaultdict(int)
        
        for num in nums:
            # current prefix sum
            curr_sum += num
            
            # situation 1:
            # continuous subarray starts 
            # from the beginning of the array
            if curr_sum == k:
                count += 1
            
            # situation 2:
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a subarray with sum k 
            # has occurred up to the current index
            count += h[curr_sum - k]
            
            # add the current sum
            h[curr_sum] += 1
                
        return count
        


#Approach2 without extra space:
# Instead of considering all the start and end points and then finding the sum for each subarray corresponding to those points, we can directly find the sum on the go while considering different end points. i.e. We can choose a particular start point and while iterating over the end points, we can add the element corresponding to the end point to the sum formed till now.
# TIme O(n2) spaceO(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                if sm == k:
                    count += 1
        return count
# Appraoch 1 prefix sum O(n2) soln:
# Time O(n2): space O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        [1, 2,1, 4]
        i = 0, j= 0
        first iteration total sum + storing left sum of all indeces in different array of equal size
        next iteration
        n2 combination -> totalsum - leftfirst-(total- left-last) == k
            left_b+ b -left_a == k
        """
        res = 0
        sm = [0] * (len(nums) + 1)
        for i in range(1, len(nums) +1):
            sm[i] = sm[i-1]+ nums[i-1]
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if sm[j+1] -sm[i] == k:
                    res += 1
        return res