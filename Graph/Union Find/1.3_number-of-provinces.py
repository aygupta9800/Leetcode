# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

#Approach1 Time complexity : O(n^3). We traverse over the complete matrix once. Union and find operations take O(n) time in the worst case.
# Space complexity : O(n). parent array of size n is used.
# But with path compression and size optimisation totalcompexity = O(n^2) * O(1)= O(n2)
class Solution:
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(A):
            root = A
            while par[root] != root:
                root = par[root]
            while par[A] != root:
                old_root = par[A]
                par[A] = root
                A = old_root
            return root
        
        def union(A, B):
            root_A = find(A)
            root_B = find(B)
            if root_A == root_B:
                return False
            if rank[root_A] <= rank[root_B]:
                par[root_A] = root_B
                rank[root_B] += rank[root_A]
            else:
                par[root_B] = root_A
                rank[root_A] += rank[root_B]
            return True
        
        count = n
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1 and union(i,j):
                    count -= 1
        return count
                    
#DFS soln
# O(n2) TIme complexity- matrix size = n*n
# space O(n) . visited array of size n is used.
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        def dfs(M, visit, i):
            if i in visit:
                return False
            visit.add(i)
            for j in range(n):
                if M[i][j] == 1 and j not in visit:
                    dfs(M, visit, j)
            return True
                
        
        visit = set()
        count = 0
        for i in range(n):
            if i in visit:
                continue
            # print("===")
            dfs(isConnected, visit, i)
            count += 1
        return count
                
        
        
        
        
        