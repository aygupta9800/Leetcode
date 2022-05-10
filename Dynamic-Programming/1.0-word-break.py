# Need to learn dp, memoization and bfs approach to solve 
# the problem

#approach 3: dp topdown, looping from backward
# time: O(n2* m) where n is len of string and m is len of dic
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # easier way to loop on index in reverse order and then checking if word starting from it in dic
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[n] = True
        for i in range(n -1, -1, -1):
            for w in wordDict:
                if i+len(w) <= len(s) and s[i: i+len(w)] == w and dp[i+len(w)] == True:
                    dp[i] = True
                    break
        return dp[0]

#Approach2: Using dynamic progamming O(n3) time complexity
# O(n)space
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        BruteForce: Using recursion and backtracking
        Time Complexity: n+1* n* n-1*...1 ways to split string
        O(2^n)
        Space: O(n)- depth of the recursion max to n
        """
        word_set = set(wordDict)
        # we keep dp[i] for the word ending at i 
        # and we search till dp[i] = and d[j] true and s[j+1: i] in word dict 
        n = len(s)
        dp = [False for i in range(n)]
        dp[0] = s[0] in word_set
        for i in range(1, len(s)):
            for j in range(i):
                if s[:i+1] in word_set or (dp[j] and s[j+1:i+1] in word_set):
                    dp[i] = True
        return dp[len(s) -1]

# Approach 1 Using Recursion + Backtracking
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        BruteForce: Using recursion and backtracking
        Time Complexity: n+1* n* n-1*...1 ways to split string
        O(2^n)
        Space: O(n)- depth of the recursion max to n
        """
        def backtrack(s, wordDict, start):
            if start == len(s):
                return True
            for end in range(start +1 , len(s) + 1):
                if s[start:end] in wordDict and backtrack(s, wordDict, end):
                    return True
            return False
        
        return backtrack(s, set(wordDict), 0)

#BFS Soln
class Solution:
    """
     Visualize the string as a tree where each node represents the prefix upto index endend. Two nodes are connected only if the substring between the indices linked with those nodes is also a valid string which is present in the dictionary. In order to form such a tree, we start with the first character of the given string (say ss) which acts as the root of the tree being formed and find every possible substring starting with that character which is a part of the dictionary. Further, the ending index (say ii) of every such substring is pushed at the back of a queue which will be used for Breadth First Search. Now, we pop an element out from the front of the queue and perform the same process considering the string s(i+1,end)s(i+1,end) to be the original string and the popped node as the root of the tree this time. This process is continued, for all the nodes appended in the queue during the course of the process. If we are able to obtain the last element of the given string as a node (leaf) of the tree, this implies that the given string can be partitioned into substrings which are all a part of the given dictionary.
    """
    # TIme: O(n^3) For every starting index, the search can continue till the end of the given string.
    # Space complexity : O(n)O(n). Queue of at most nn size is needed.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False