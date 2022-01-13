# A word's generalized abbreviation can be constructed by taking any number of non-overlapping and non-adjacent substrings and replacing them with their respective lengths.

# For example, "abcde" can be abbreviated into:
# "a3e" ("bcd" turned into "3")
# "1bcd1" ("a" and "e" both turned into "1")
# "5" ("abcde" turned into "5")
# "abcde" (no substrings replaced)

# Input: word = "word"
# Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]

# Time complexity : O(n 2^n)
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        """
        1. skip the char,=> increase the count 
        2. keep the char=> place comb till now + count till now+ cur char
        """
        res = []
        def backtrack(first, comb, count):
            if first == len(word):
                res.append(comb+ (str(count) if count > 0 else "" ))
                return
            
            #Skip the current pos
            backtrack(first+1, comb, count +1)
            #keep the current pos
            # comb.append(str(count) if count > 0 else "" + word[first])
            backtrack(first+1, comb + (str(count) if count > 0 else "") + word[first], 0)
        
        backtrack(0, "", 0)
        return res