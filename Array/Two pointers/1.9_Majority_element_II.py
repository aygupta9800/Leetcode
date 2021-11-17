# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Example 1: # Input: nums = [3,2,3] # Output: [3]

# Example 2: # Input: nums = [1] # Output: [1]

# Example 3: # Input: nums = [1,2] # Output: [1,2]
#Boyer-Moore voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        nums: 1 2 3 2 3 2 3
        
        """
        if not nums: return []
        
        # 1st pass
        count1, count2 , candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        #2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)
        
        return result