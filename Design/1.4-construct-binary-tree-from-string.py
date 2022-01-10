# You need to construct a binary tree from a string consisting of parenthesis and integers.
# You always start to construct the left child node of the parent first if it exists

# Example
# Input: s = "4(2(3)(1))(6(5))"
# Output: [4,2,6,3,1,5]

# Example 2:
# Input: s = "4(2(3)(1))(6(5)(7))"
# Output: [4,2,6,3,1,5,7]

# Example 3:
# Input: s = "-4(2(3)(1))(6(5)(7))"
# Output: [-4,2,6,3,1,5,7]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        return self.dfs(s, 0) [0]
    
    def getNumber(self, s, i):
        sign = True
        if s[i] == '-':
            sign = False
            i += 1
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        return num if sign else -num, i
        
    
    def dfs(self, s, i):
        if i == len(s):
            return None, i
        
        #get root value
        root_val, i = self.getNumber(s, i)
        node = TreeNode(root_val)
        # first subtree will always be left acc to constraints
        if i < len(s) and s[i] == "(":
            node.left, i = self.dfs(s, i+1)
        if node.left and i < len(s) and s[i] == '(':
            node.right, i = self.dfs(s, i+1)
        return node, i + 1 if i < len(s) and s[i] == ')' else i
        
        