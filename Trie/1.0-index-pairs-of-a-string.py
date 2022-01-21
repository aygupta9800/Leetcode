#https://leetcode.com/problems/index-pairs-of-a-string/

# Given a string text and an array of strings words, return an array of all index pairs [i, j] so that the substring text[i...j] is in words.

# Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).

# Example 1:

# Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
# Output: [[3,7],[9,13],[10,17]]
# Example 2:

# Input: text = "ababa", words = ["aba","ab"]
# Output: [[0,1],[0,2],[2,3],[2,4]]
# Explanation: Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].

# Time complexity O(n*s) whenre s is len of text and n is no. of words
# space complexity O(n) where n is total no. of words
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        result = []
        for i in range(len(text)):
            self.traverse(i, text, result, trie)
        
        return result
    
    def traverse(self, start, text, result, trie):
        curr = trie.root
        for end in range(start, len(text)):
            c = text[end]
            if c not in curr.children:
                return False
            curr= curr.children[c]
            if curr.word:
                result.append([start, end])