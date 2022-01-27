# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Q. you are given an integer array nums with no duplicates.A maximum binary tree
# can be built recursively from nums using the following algorithm:
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.

#Approach2 : Using Monotonic stack:
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Approach 2 Using stack:
        The key idea is:
1. We scan numbers from left to right, build the tree one node by one step;
2. We use a stack to keep some (not all) tree nodes and ensure a decreasing order;
3. For each number, we keep pop the stack until empty or a bigger number;
 The bigger number (if exist, it will be still in stack) is current number's root,
and the last popped number (if exist) is current number's left child (temporarily,
this relationship may change in the future); Then we push current number into the stack.

        """
        stack = []
        for i in range(len(nums)):
            curr = TreeNode(nums[i])
            # assign left relationship until we find bigger number or empty stack
            while stack and stack[-1].val < curr.val:
                curr.left = stack[-1]
                stack.pop()
            if stack:
                stack[-1].right = curr
                
            stack.append(curr)
        
        # Return the first elem i.e bottom of array as that will be max root of binary tree
        return stack[0]



# Approach1 Divide and conquer
# Time O(n2), space O(n)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        nums = [3,2,1, 6, 0,5]
        find max = O(n)
        root.val = max
        root.left = same fn(0, maxi-1)
        root.right = same fn(max_i+1, n-1)
        
        """
        def getMax(l, r):
            max_i = l
            for i in range(l, r+1):
                if nums[max_i] < nums[i]: max_i = i
            return max_i
        
        def construct(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            max_i = getMax(l,r)
            root = TreeNode(nums[max_i])
            root.left= construct(l, max_i-1)
            root.right = construct(max_i+1, r)
            return root
        
        return construct(0, len(nums) -1)
        
        