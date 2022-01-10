#Approach 3: Using Dynamic Programming
# O(n) time O(n) space
class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        """
        Recursion with memoization
        """
        # Special handling for empty case.
        if not nums:
            return 0
        maxRobbedAmount = [None for _ in range(len(nums) +1)]   
        N = len(nums)
        #Base case initialization
        maxRobbedAmount[N], maxRobbedAmount[N-1] = 0, nums[N-1]
        #DP table calculations.
        for i in range(N-2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i+1], maxRobbedAmount[i+2] + nums[i])
        return maxRobbedAmount[0]

#Approach4: Optimized DP- spaceO(1) timeO(n)
class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        """
        Instead of keeping an entire table for storing these cached values,
        we can get by with simply keeping track of the "next" two values.
        """
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        maxRobbedAmount = [None for _ in range(len(nums) +1)]
            
        N = len(nums)
        
#         #Base case initialization
#         maxRobbedAmount[N], maxRobbedAmount[N-1] = 0, nums[N-1]
        
        rob_next = nums[N-1]
        rob_next_plus_one = 0
        #DP table calculations.
        for i in range(N-2, -1, -1):
            # maxRobbedAmount[i] = max(maxRobbedAmount[i+1], maxRobbedAmount[i+2] + nums[i])
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            #Upadte variables
            rob_next_plus_one = rob_next
            rob_next = current
        
        return rob_next
        

#Approach 2: Using recursion with memoization
class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:  
        n = len(nums) - 1
        def calculateMax(nums, left):
            if left > n:
                return 0
            # Return cached value
            if left in self.memo:
                return self.memo[left]
            
            #Recursive relation evaluation to get optimal answer
            res1 = nums[left] + calculateMax(nums,left +2 )
            res2 = calculateMax(nums, left + 1)
            ans = max(res1, res2)
            self.memo[left] = ans
            return ans
        
        return calculateMax(nums, 0)
  

#Approach 1
#BRuteforce reducint to subproblem using recursion
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        """
        n = len(nums) - 1
        def calculateMax(nums, left):
            if left > n:
                return 0
            res1 = nums[left] + calculateMax(nums,left +2 )
            res2 = calculateMax(nums, left + 1)
            return max(res1, res2)
        
        return calculateMax(nums, 0)
        