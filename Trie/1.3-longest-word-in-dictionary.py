# Time Complexity: O(∑w_i), where w_i is the length of words[i].
# This is the complexity to build the trie and to search it.

# If we used a BFS instead of a DFS, and ordered the children in an array,
# we could drop the need to check whether the candidate word at each node is better
# than the answer, by forcing that the last node visited will be the best answer.

# Approach 2 Using Trie:
# Space Complexity: O(∑w_i), the space used by our trie.
class TrieNode:
    def __init__(self):
        # self.children = {}
        self.children = defaultdict(TrieNode)
        self.eow = -1 # from 0 to len(word) -1 index we will map if word
    
class Solution():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, index):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.eow = index
    
    def dfs(self, words):
        ans = ""
        stack = []
        stack.append(self.root)
        while stack:
            node = stack.pop()
            # either root node or end of a word as we need to build word by
            # one character at a time by other words in words.
            if node.eow > -1 or node == self.root:
                if node != self.root:
                    word = words[node.eow]
                    #checking lexicographical order if same len
                    if len(word) > len(ans) or \
                    (len(word) == len(ans) and word < ans):
                        ans = word
                for nei in node.children.values():
                    stack.append(nei)
        return ans
        
    def longestWord(self, words: List[str]) -> str:
        # trie = self.root
        index = 0
        for word in words:
            self.insert(word, index)
            index += 1
        # self.words = words
        return self.dfs(words)

# Approach3 Alternative way to write dfs recursive
def dfs(self, words, node):
    """
    keep a stack for dfs, insert root
    pop it and check if its worth exploring the node children
    that is if node is word or root
    then if word, check if len(word) > len(ans) or if equal len, its
    lexi smaller, then add to result and then add all its nei in stack
    return ans
    """
    if node is self.root or node.eow > -1:
        if node != self.root:
            word = words[node.eow]
            if len(word) > len(self.ans) or \
            (len(word) == len(self.ans) and word < self.ans):
                self.ans = word
        for nei in node.children.values():
            self.dfs(words, nei)
def longestWord(self, words: List[str]) -> str:
    index = 0
    for word in words:
        self.insert(word, index)
        index += 1
    self.ans = ""
    self.dfs(words, self.root)
    return self.ans


# Approach 1 Approach #1: Brute Force [Accepted]
# Intuition
# For each word, check if all prefixes word[:k] are present.
# We can use a Set structure to check this quickly.
# Time: O(∑w_i)^2, where w_i is the length of words[i]. Checking whether all prefixes of words[i]
# are in the set is O(∑w_i)^2

# Space complexity : O(∑w_i)^2 to create the substrings.
class Solution(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in xrange(1, len(word))):
                    ans = word

        return ans
        
        
        