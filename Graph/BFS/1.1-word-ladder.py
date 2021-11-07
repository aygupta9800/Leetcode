# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence

                # BFS     #adj list
# Time complexity O(n*2 m)+ O(n*m2) m is len of word, n len of wordlist, space complexity O(m * n2)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        neiList = collections.defaultdict(list)
        # Making adjacency list using pattern hot *ot, h*t, ho* , dot has *ot, d*t, do* so 1 common patttern 
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j]+"*"+w[j+1:]
                neiList[pattern].append(w)

        # Running BFS as it is more efficient approach for shortest path problems
        visit = set([beginWord])
        q= deque([beginWord])
        res = 1
        while q:
            qLen = len(q)
            for i in range(qLen):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j]+ "*"+ word[j+1:]
                    for nei in neiList[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            #Adding len of path after each level
            res += 1
        # If endword is not found 
        return 0


# Constraints:
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
                    
        
        
        