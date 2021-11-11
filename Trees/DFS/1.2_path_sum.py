#with DFS Recursion
# Time complexity : we visit each node exactly once, thus the time complexity is \mathcal{O}(N)O(N), where NN is the number of nodes.
# Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only one child node, the recursion call would occur NN times (the height of the tree),
# therefore the storage to keep the call stack would be \mathcal{O}(N)O(N). But in the best case (the tree is completely balanced), the height of the tree would be \log(N)log(N). Therefore, the space complexity in this case would be \mathcal{O}(\log(N))O(log(N)).

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

#with DFS iteration
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum- root.val),]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum -node.left.val))
            
        return False