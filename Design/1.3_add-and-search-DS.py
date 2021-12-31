# Time complexity:
# Time complexity: O(M) for the "well-defined" words without dots, where M is the key length, and N is a number of keys, and O(N⋅26^M) for the "undefined" words. That corresponds to the worst-case situation of searching an undefined word \underbrace{.........}_\text{M times} 
# M times
# .........
# ​
 
# ​
#   which is one character longer than all inserted keys.

# Space complexity: O(1) for the search of "well-defined" words without dots, and up to O(M) for the "undefined" words, to keep the recursion stack.



class TrieNode:
    def __init__(self):
        self.children = {} # a: TrieNode
        self.word = False #TO mark end of the word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.word
        return dfs(0, self.root)

