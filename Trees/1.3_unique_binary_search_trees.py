# Given an integer n, return the number of structurally unique BST's (binary search trees)
# which has exactly n nodes of unique values from 1 to n.
class Solution:
    def numTrees(self, n: int) -> int:
        """
        numsTrees[4] = numsTrees[0]* numsTrees[3]
            + numsTrees[1] * numsTrees[2]
            + numsTrees[2] * numsTrees[1]
            + numsTrees[3] * numsTrees[0]
        """
        numTree = [1] * (n+1)
        for node in range(2, n+1):
            total = 0
            # keeping node as number of elements in tree, we pick one root through loop
            for root in range(1, node+1):
                left = root -1
                right = node- root
                total += numTree[left] * numTree[right]
            numTree[node] = total
        return numTree[n]