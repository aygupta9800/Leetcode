# https://leetcode.com/problems/implement-trie-prefix-tree/solution/
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    # Insert: Time O(m), space O(m) => m is length of keys in word
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True
    # Search: Time O(m), space O(1)
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.eow
        
    # Search: Time O(m), space O(1)
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)