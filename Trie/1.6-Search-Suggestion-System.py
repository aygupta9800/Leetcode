# Time complexity : O(M) to build the trie where M is total number of characters in products For each prefix we find its representative node in O(\text{len(prefix)})O(len(prefix)) and dfs to find at most 3 words which is an O(1) operation. Thus the overall complexity is dominated by the time required to build the trie.

# In Java there is an additional complexity of O(m^2)O(m 
# 2
#  ) due to Strings being immutable, here m is the length of searchWord.
# Space complexity : O(26n)=O(n)O(26n)=O(n). Here n is the number of nodes in the trie. 26 is the alphabet size. Space required for output is O(m)O(m) where m is the length of the search word.


class TrieNode:
    
    def __init__(self):
        self.isWord = False
        # for pre order traversal, we inset char in order through order
        self.children = [None] * 26
    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        self.root = TrieNode()
        
        def insert(s):
            curr = self.root
            
            for c in s:
                if curr.children[ord(c) - ord('a')] == None:
                    curr.children[ord(c)-ord('a')] = TrieNode()
                curr = curr.children[ord(c)-ord('a')]
            
            curr.isWord = True
            
        def dfsFromNode(node, curWord, result):
            
            # print('CAlling dfs')
            
            if len(result) == 3:
                return 
            
            # print("isWord")
            # print(curWord)
            if node.isWord:
                result.append(curWord)
            
            for cAsci in range(ord('a'), ord('z') +1):
                c = chr(cAsci)
                if node.children[ord(c)- ord('a')]:
                    dfsFromNode(node.children[ord(c)- ord('a')], curWord+c, result)
                    
            
        
        def getWordsStartingWith(prefix):
            curr = self.root
            resultBuffer = []
            # Move curr to the end of prefix in its trie representation.
            for c in prefix:
                if curr.children[ord(c)-ord('a')] == None:
                    return resultBuffer
                curr = curr.children[ord(c)-ord('a')]
            
            dfsFromNode(curr, prefix, resultBuffer)
            # print('buffer')
            # print(resultBuffer)
            return resultBuffer
            # dfs from the node to find words in preorder
            # dfsWithPrefix(cur)
        
        result = []
        for w in products:
            insert(w)
        
        prefix = ''
        for c in searchWord:
            prefix += c
            result.append(getWordsStartingWith(prefix))
        print(result)
        return result
                
            
        