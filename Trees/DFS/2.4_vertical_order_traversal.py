

#Approach3: 
# The key insight is that we only need to know the range of the column index (i.e. [min_column, max_column]). Then we can simply iterate through this range to generate the outputs without the need for sorting.
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levelMap = defaultdict(list)
        min_column = max_column = 0
        q = deque([(root, 0)])
        while q:
            node, column = q.popleft()

            if node is not None:
                levelMap[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                q.append((node.left, column - 1))
                q.append((node.right, column + 1)) 
            #   since values in col will already be sorted colm wise due to lvel order travesal, we just need to sort which col keys comes first
            # TIme O(nlogn)
        return [levelMap[x] for x in range(min_column, max_column+1)]



#Approach2 BFS with extra space 
# Time Complexity: O(NlogN) where N is the number of nodes in the tree.
#space O(n) complexity
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        levelMap = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, column = q.popleft()

            if node is not None:
                levelMap[column].append(node.val)
                q.append((node.left, column - 1))
                q.append((node.right, column + 1)) 
            #   since values in col will already be sorted colm wise due to lvel order travesal, we just need to sort which col keys comes first
            # TIme O(nlogn)
        return [levelMap[x] for x in sorted(levelMap.keys())]

# Approach 1 DFS:
# Time Complexity: O(W⋅HlogH)) where W is the width of the binary tree (i.e. the number of columns in the result) and H is the height of the tree.
# In the first part of the algorithm, we traverse the tree in DFS, which results in O(N) time complexity.
# Once we build the columnTable, we then have to sort it column by column.

# Space Complexity: O(N) where N is the number of nodes in the tree.
# We kept the columnTable which contains all the node values in the binary tree. Together with the keys, it would consume O(N) space as we discussed in previous approaches.
# Since we apply the recursion for our DFS traversal, it would incur additional space consumption on the function call stack. In the worst case where the tree is completely imbalanced, we would have the size of call stack up to O(N).
# Finally, we have the output which contains all the values in the binary tree, thus 
# O(N) space.
# So in total, the overall space complexity of this algorithm remains O(N).
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levelMap = defaultdict(list)
        min_col = max_col =0
        def dfs(node, row, col):
            if not node:
                return
            nonlocal min_col, max_col
            levelMap[col].append((row, node.val))
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            dfs(node.left, row+1, col -1)
            dfs(node.right, row+1, col +1)
        
        dfs(root, 0, 0)
        # order by colm and sort by row
        # level = [val for key, val in sorted(levelMap.items())]
        # return level
        ret = []
        # O(W) operation
        for col in range(min_col, max_col+1):
            #O(HlogH)operation
            levelMap[col].sort(key= lambda x: x[0])
            colVals= [val for row, val in levelMap[col]]
            ret.append(colVals)
        return ret