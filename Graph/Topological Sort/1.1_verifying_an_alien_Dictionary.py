# TIme complexity O(N+M) = O(M) as N = 26
# N is len of order, M is len of characters in all the words
# For the nested for-loops, we examine each pair of words in the outer-loop and for the inner loop, we check each letter in the current word. Therefore, we will iterate over all of letters in words.
# space O(N) = O(1) as n = 26
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #O(N)
        orderMap = { n: i for i, n in enumerate(order)}
        
        #o(M)
        for i in range(len(words) -1):
            w1, w2 = words[i], words[i+1]
            for x in range(len(w1)):
                if x ==len(w2):
                    return False
                if w1[x] != w2[x]:
                    if orderMap[w2[x]] < orderMap[w1[x]]:
                        return False
                    break
        return True