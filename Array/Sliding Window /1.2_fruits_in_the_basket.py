# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on
#  the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree)
# while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

#Logic: we keep navigating from start with two pointers and keep track of elem and its last visited indic in dic
# as soon as we encounter 3rd distinct elem in dic, we delte the key with min index value so to have only last 2 visited
# type of fruit.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = end =0
        max_len = 0
        dic = {}
        
        while end < len(fruits):
            dic[fruits[end]] = end
            if len(dic) > 2:
                min_value = min(dic.values())
                del dic[fruits[min_value]]
                start = min_value + 1
            max_len = max(max_len, end- start +1)
            end += 1
        return max_len
            
                