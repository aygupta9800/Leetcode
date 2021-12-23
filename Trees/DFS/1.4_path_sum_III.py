# Given the root of a binary tree and an integer targetSum, return the number of paths
#  where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, 
# but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Approach 2
#Using Prefix Sum O(n)
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder (node: TreeNode, curSum) -> None:
            nonlocal count
            if not node:
                return
            
            #current prefix sum
            curSum += node.val
            
            #if from start to current total sm is k:
            if curSum == k:
                count += 1
                
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a path with sum k 
            # has occurred up to the current node
            count += prefixSums[curSum - k]
            
            # to add curr_sum to map
            prefixSums[curSum] += 1
            
            #process the left subtree
            preorder(node.left, curSum)
            preorder(node.right, curSum)
            
            # remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing\
            prefixSums[curSum] -= 1
            
        count, k = 0, targetSum
        prefixSums = defaultdict(int)
        preorder(root, 0)
        return count
            


# Using Recursion:
# Time Complexity O(n2) space O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathSum_a(root, sm):
            if root is None:
                return 0
            res = 0
            if root.val == sm:
                res += 1
            res += pathSum_a(root.left, sm-root.val)
            res += pathSum_a(root.right, sm-root.val)
            
            return res
        
        if root is None:
            return 0
        return self.pathSum(root.left, targetSum)+ self.pathSum(root.right, targetSum)+ pathSum_a(root, targetSum)

#Time complexity O(n2)
class Solution:
    def helper(self, root, sum, lst, count):
        lst.append(root.val)
        if root.left:
            count = self.helper(root.left, sum, lst, count)
        if root.right:
            count = self.helper(root.right, sum, lst, count)
        """
        The trick is to check the sum of path from bottom node to current node and check how many can have same sum
        """
        temp = 0
        for i in range(len(lst)-1, -1, -1):
            temp += lst[i]
            if temp == sum:
                count +=1
        lst.pop()
        return count
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        return self.helper(root, targetSum, [], 0)
        