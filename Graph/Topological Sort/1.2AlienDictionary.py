# PS:
# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

#Time complexity => O(C)n => c total charcters in words
# Building the adjacency list has a time complexity of O(C) for the same reason as in Approach 1.

# WITH Kanhns/ BFS
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w}
        in_degree = Counter({c : 0 for w in words for c in w})
#       Formation of adjacency list
        for i in range(len(words) -1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[: minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] +=1
                    break
        #taken
        res = []
        #cantake queue
        q = deque([c for c in in_degree if in_degree[c] == 0])
        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                in_degree[nei] -=1
                if in_degree[nei] == 0:
                    q.append(nei)
        # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
        # print(res)
        if len(res) < len(in_degree):
            return ""
        return "".join(res)





# Again, like in Approach 1, we traverse every "edge", but this time we're using depth-first-search.
# Space complexity : O(1) or O(U+min(U2,N)).
# we can build reverse adj list in that case we wont need to reverse the result of dfs.

# One issue we need to be careful of is cycles. In directed graphs, we often detect cycles by using graph coloring. All nodes start as white(Not in visit), and then once they're first visited they become grey(visted TRUE), and then once all their outgoing nodes have been fully explored(visited FALSE), they become black. We know there is a cycle if we enter a node that is currently grey(Visited TRUE) (it works because all nodes that are currently on the stack are grey. Nodes are changed to black when they are removed from the stack).


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w} 
#       Formation of adjacency list
        for i in range(len(words) -1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[: minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # False= visited, True = in Path
        # in path and if we again see same node then its loop
        # post order traversal is needed for DAG 
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
            
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

        