# Time complexity: O(M(4⋅3^L−1), where M is the number of cells in the board
#  and L is the maximum length of words.

# space complexity:  \mathcal{O}(N)O(N), where NN is the total number of letters in the dictionary.

# Note: Optimization
# Gradually prune the nodes in Trie during the backtracking.

# The idea is motivated by the fact that the time complexity of the overall algorithm sort of depends on the size of the Trie.
# For a leaf node in Trie, once we traverse it (i.e. find a matched word),
# we would no longer need to traverse it again. As a result, we could prune it out
# from the Trie. Gradually, those non-leaf nodes could become leaf nodes later, since we trim their children leaf nodes.
# In the extreme case, the Trie would become empty, once we find a match for all the words in the dictionary.
# This pruning measure could reduce up to 50\%50% of the running time for the test cases of the online judge

# Approach2 Backtracking+ Trie+ Optimization
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.eow = False
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            # defaultdict so no need to check if exist
            cur = cur.children[c]
        # adding word at end instead of true so that we dont need to keep track of prefix in dfs
        cur.eow = word
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
        
        m, n = len(board), len(board[0])
        # visit = set()
        res = []
        
        def backtrack(r,c, node):
            if r < 0 or r == m or c < 0 or c == n or (r,c) == "#" \
            or board[r][c] not in node.children:
                return False
            
            curLetter = board[r][c]
            curNode = node.children[curLetter]
            #mark the current node to use it as visit
            # visit.add((r,c))
            board[r][c] = "#"
            if curNode.eow:
                res.append(curNode.eow)
                # if matched word is leaf node in trie
                if not curNode.children:
                    node.children.pop(curLetter)
                else:
                    # so that we dont again add same word in the res
                    curNode.eow = False
            lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for row, col in lst:
                backtrack(row, col, curNode)
            board[r][c] = curLetter
            # visit.remove((r,c))
            
            # node.children.pop(curLetter)
            # if not curNode:
            #     node.children.pop(curLetter)
        
        for r in range(m):
            for c in range(n):
                backtrack(r,c, self.root)
        
        return list(res)
        
        

# Approach 1 Using Trie+ backtracking+  not optimised
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.eow = False
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            # defaultdict so no need to check if exist
            cur = cur.children[c]
        cur.eow = True
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
        
        m, n = len(board), len(board[0])
        visit = set()
        res = set()
        def backtrack(r,c, word, node):
            # print(2)
            if r < 0 or r == m or c < 0 or c == n or (r,c) in visit or board[r][c] not in node.children:
                return False
            visit.add((r,c))
            if node.children[board[r][c]].eow:
                res.add(word+board[r][c])
            lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for row, col in lst:
                backtrack(row, col, word+board[r][c], node.children[board[r][c]])
            visit.remove((r,c))
        
        for r in range(m):
            for c in range(n):
                backtrack(r,c, "", self.root)
        
        return list(res)
        
        