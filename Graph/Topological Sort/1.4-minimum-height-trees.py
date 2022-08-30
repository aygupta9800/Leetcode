class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        For the tree-alike graph, the number of centroids is no more than 2.
        """
        if n <= 2:
            return [i for i in range(n)]
        
        adj = defaultdict(set)
        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)
        
        #First leaf layer
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
                
        #trim till leaves reaching centroid
        remainingNodes = n
        while remainingNodes > 2:
            remainingNodes -= len(leaves)
            newLeaves = []
            #remove the current leaf edges
            while leaves:
                leaf = leaves.pop()
                nei = adj[leaf].pop()
                adj[nei].remove(leaf)
                if len(adj[nei]) == 1:
                    newLeaves.append(nei)
                
                # prepare for next round
            leaves = newLeaves
        # remaining centroid are the centroids of the graph
        return leaves
        