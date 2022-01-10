#Approach2 : Using Reverse
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        first reverse whole array
        then reverse first k elememnts and remaining n-k elements
        """
        def reverse(nums: list, start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
                
        n = len(nums)
        k %= n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

#Approach 1: Using cyclic replacement
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        In case n%k == 0 we have to update index += 1when we reach start index
        we have to do replacement n times
        """
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            prev_i, prev = start, nums[start]
            while True:
                new_i = (prev_i + k) % n
                
                #swap prev and new no.
                nums[new_i], prev = prev, nums[new_i]
                
                prev_i = new_i
                count += 1
                
                if start == prev_i:
                    break
            start += 1
                
        