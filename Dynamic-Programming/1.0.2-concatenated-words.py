# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

# Approach 1
class CompoundWords:
    def getComb(self, word, first, wordset):
        n = len(word)
        if first == len(word):
            return True
 
        subWord = ""
        for i in range(first, n):
            subWord += word[i]
            if subWord in wordset:
                isWord = self.getComb(word, i+1, wordset)
                if isWord:
                    return True

        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res= []
        wordset = set(words)
        for word in words:
            wordset.remove(word)
            isWord =  self.getComb(word, 0, wordset)
            if isWord:
                res.append(word)
            wordset.add(word)
        return res


# Approach ---for finding all combinations
# Input: [rockstar, rock, stars, rocks, tar, star, rockstars, super, highway, high, way, superhighway]
# Output: [[rock, star], [rocks, tar], [super, highway], [super, high, way],...]
# Solution for finding all the concatenated words combinations:
class Solution:

    def getComb(self, word, first, currList, wordset, wordRes):
        n = len(word)
        if first == len(word):
            wordRes.append(currList[::])
 
        # curr_word = ""
        for i in range(first, n):
            # curr_word += word[i]
            subWord = word[first: i+1]
            if subWord in wordset:
                # currList.append(subWord)
                # wordset
                self.getComb(word, i+1, currList+[subWord], wordset, wordRes)
                # currList.remove(subWord)


    def findComb(self, wordList):
        res= []
        wordset = set(wordList)
        for word in wordList:
            wordset.remove(word)
            comb = []
            self.getComb(word, 0, [], wordset, comb)
            if len(comb) > 0:
                res.extend(comb)
            wordset.add(word)
        return res

        
        