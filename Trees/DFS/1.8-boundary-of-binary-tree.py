# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Approach2
# preorder traversal with help of flag tracking for different nodes:
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        def isLeaf(node):
            return not node.left and not node.right
    
        def isLeftBoundary(flag):
            return flag == 1
    
        def isRightBoundary(flag):
            return flag == 2
        
        def isRoot(flag):
            return flag == 0
        
        # what will be the flag of left child
        def leftChildFlag(curr, flag):
            if isLeftBoundary(flag) or isRoot(flag):
                return 1
            elif isRightBoundary(flag) and not curr.right:
                return 2
            else: return 3
        
        def rightChildFlag(curr, flag):
            if isRightBoundary(flag) or isRoot(flag):
                return 2
            elif isLeftBoundary(flag) and not curr.left:
                return 1
            else: return 3
        
        def dfs(curr, leftBoundary, rightBoundary, leaves, flag):
            if not curr:
                return
            
            if isLeaf(curr):
                leaves.append(curr.val)
            elif isRightBoundary(flag):
                rightBoundary.append(curr.val)
            elif isLeftBoundary(flag) or isRoot(flag):
                leftBoundary.append(curr.val)
                
            dfs(curr.left, leftBoundary, rightBoundary, leaves, leftChildFlag(curr, flag))
            dfs(curr.right, leftBoundary, rightBoundary, leaves, rightChildFlag(curr,flag))
        
        leftBoundary = []
        rightBoundary = []
        leaves = []
        dfs(root, leftBoundary, rightBoundary, leaves, 0)
        # leftBoundary + = leaves + rightBoundary[::-1]
        
        return leftBoundary + leaves + rightBoundary[::-1]


# Approach 1: 
# simply first find left boundary then leaves then right in seperate iteration then
# append all the result
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        def isLeaf(node):
            return not node.left and not node.right
        
        def addLeaves(res, node):
            if isLeaf(node):
                res.append(node.val)
                return
            if node.left:
                addLeaves(res, node.left)
                
            if node.right:
                addLeaves(res, node.right)
            
        
        res = []
        if not root: return None
        
        if not isLeaf(root):
            res.append(root.val)
        
        leftBoundaryNode = root.left
        
        while leftBoundaryNode:
            if not isLeaf(leftBoundaryNode):
                res.append(leftBoundaryNode.val)
            if leftBoundaryNode.left:
                leftBoundaryNode = leftBoundaryNode.left
            else:
                leftBoundaryNode = leftBoundaryNode.right
        
        # add leaves to the result
        addLeaves(res, root)
        
        
        # add right boundary to the result but in rev order
        stack = []
        rightBNode = root.right
        
        while rightBNode:
            if not isLeaf(rightBNode):
                stack.append(rightBNode.val)
            if rightBNode.right:
                rightBNode = rightBNode.right
            else:
                rightBNode = rightBNode.left
        
        if stack:
            res.extend(stack[::-1])
            
        return res
        
                
            