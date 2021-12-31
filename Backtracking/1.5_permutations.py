class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            # base condn
            if first == n:
                output.append(nums[:])
            
            for i in range(first, n):
                # place i-th integer first in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutation
                backtrack(first +1)
                #backtrack
                nums[first], nums[i] = nums[i], nums[first]
            
        n = len(nums)
        output = []
        backtrack()
        return output


# Time complexity : O(∑k=1toN P(N,k)) where P(N, k) = \frac{N!}{(N - k)!} = N (N - 1) ... (N - k + 1)P(N,k)= 
# (N−k)!N! = N(N−1)...(N−k+1) is so-called k-permutations_of_n, or partial permutation.
# Here first + 1 = k for the expression simplicity. The formula is easy to understand : for each kk (each firstfirst) one performs N(N - 1) ... (N - k + 1)N(N−1)...(N−k+1) operations, and kk is going through the range of values from 11 to NN (and firstfirst from 00 to N - 1N−1).

# Let's do a rough estimation of the result : N! \le \sum_{k = 1}^{N}{\frac{N!}{(N - k)!}} = \sum_{k = 1}^{N}{P(N, k)} \le N \times N!N!≤∑ 
# k=1 toN (N−k)! N! =∑ P(N,k) ≤ N×N!, i.e. the algorithm performs better than O(N×N!) and a bit slower than O(N!).

# Space complexity : O(N!) since one has to keep N! solutions.
