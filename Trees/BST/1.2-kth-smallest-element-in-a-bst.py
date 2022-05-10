# Given the root of a binary search tree, and an integer k, return the kth smallest
# value (1-indexed) of all the values of the nodes in the tree.

# Approach 2 ITerative 
# Time complexity: O(H + k)O(H+k), where H is a tree height. This complexity is defined by the stack, which contains at least H + kH+k elements, since before starting to pop out one has to go down to a leaf. This results in O(\log N + k)O(logN+k) for the balanced tree and O(N + k)O(N+k) for completely unbalanced tree with all the nodes in the left subtree.

# Space complexity: O(H)O(H) to keep the stack, where HH is a tree height. That makes O(N)O(N) in the worst case of the skewed tree, and O(\log N)O(logN) in the average case of the balanced tree.
class Solution:
    """
    controlled recursion by using iterative approach
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        while curr and stack:
            # Append all the left elem of root for inorder traversal
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            # as root and root.left must have already poped up
            # append right subtree of root into stack for inorder traversal
            curr = curr.right



#ANother solution
class Solution:
    """
    controlled recursion by using iterative approach
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            # Append all the left elem of root for inorder traversal
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -=1
            if not k:
                return root.val
            # as root and root.left must have already poped up
            # append right subtree of root into stack for inorder traversal
            root = root.right

# Approach 1 Recursive+ inorder traversal
# time complexity: O(n), space: o(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(r):
            return inorder(r.left)+ [r.val]+ inorder(r.right) if r else []
        return inorder(root)[k-1]