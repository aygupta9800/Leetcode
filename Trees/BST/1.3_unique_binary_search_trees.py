# Given an integer n, return the number of structurally unique BST's (binary search trees)
# which has exactly n nodes of unique values from 1 to n.
class Solution:
    def numTrees(self, n: int) -> int:
        """
        1 2 3 4 => consider each node as root node in BST
        numsTrees[4] = numsTrees[0]* numsTrees[3]
            + numsTrees[1] * numsTrees[2]
            + numsTrees[2] * numsTrees[1]
            + numsTrees[3] * numsTrees[0]
        """
        # numTree = [1] * (n+1)
        dp = [1]*(n+1)
        # dp[0], dp[1] = 1
        for node in range(2, n+1):
            total = 0
            # keeping node as number of elements in tree, we pick one root through loop
            for root in range(1, node+1):
                left = root -1
                right = node- root
                total += dp[left] * dp[right]
            dp[node] = total
        return dp[n]