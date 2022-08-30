# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach2 : Recursion with index mapping
# Time O(n) Space O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # index of left and right in-order range
        def arrayToTree(left, right):
            nonlocal pIndex
            # if there are no elem to constructs the tree
            if left > right: return None
            
            # select the pindex element as the root and increments it
            rootVal = preorder[pIndex]
            root = TreeNode(rootVal)
            pIndex += 1
            
            #build left and right subtree
            root.left = arrayToTree(left, inorderMap[rootVal] -1)
            root.right = arrayToTree(inorderMap[rootVal]+1, right)
            
            return root
    
        #preorderIndex
        pIndex = 0
        # build a hashmap to store value -> its index in inorder array
        # so that we can find inorder index of val in constant time in every level
        inorderMap = {}
        for i, val in enumerate(inorder):
            inorderMap[val] = i
        return arrayToTree(0, len(inorder) -1)
    
#Approach 2 with indexes of inorder without slicing
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Approach 1: Recursive
        """
        # based on inorder index:
        pIndex = 0
        def arrayToTree(left, right):
            nonlocal pIndex
            # if not preorder or not inorder:
            #     return None
            if left > right:
                return None
            root = TreeNode(preorder[pIndex])
            mid = inorder.index(preorder[pIndex])
            pIndex += 1
            root.left = arrayToTree(left, mid-1)
            root.right = arrayToTree(mid+1, right)
            return root
        
        return arrayToTree(0, len(inorder) - 1)
        

# Approach 1 Recursive with list slicing O(n2) time complexity
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
        