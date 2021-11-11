# Given an array of integers nums and an integer target, return indices of the
#  two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and
#  you may not use the same element twice.
# You can return the answer in any order.

# Time complexity: O(n). We traverse the list containing nn elements only once. Each lookup in the table costs only O(1)O(1) time.
# Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.

class solution:
    def twoSum(self, nums: List[int], target:int) ->List[int]:
        prevMap= {}
        for i, n in enumerate(nums):
            diff= target- n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return