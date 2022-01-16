# house robber with now houses in circle so that last house is 
# attached to first house

# we can divide this problem into 2 part.
# rob from 0 to n-2 or 1 to n -1

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))
 
    def rob_simple(self, nums):
        # 2 ways to code. start from end, or from first
        # 1. way
        N = len(nums)
       #Base case initialization(starting from end)
        
        rob_next = nums[N-1]
        rob_next_plus_one = 0
        #DP table calculations.
        for i in range(N-2, -1, -1):
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            #Upadte variables
            rob_next_plus_one = rob_next
            rob_next = current
        
        return rob_next
        #2. way
        # """
        # Imagine 2 pts t1 and t2 such that
        # first t1 robs a house then leaves a note and move onto next(2) house. and calculate value based on t2 which is 2 behind the current pos and current. then t2 moves to next house(1).
        # this way whenever t1 calculates, t2 is 2 behind
        # """
        # t1 = 0
        # t2 = 0
        # for current in nums:
        #     temp = t1
        #     t1 = max(current+ t2, t1)
        #     t2 = temp
        
        # return t1
    