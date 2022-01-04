# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

# Make a hashmap which have collison for same sequence
#Approach 1: By shifting first char to a for every string and shifting all ch with same shift
#Approach 2. Having hash with diff of succes char 
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shift_letter(c, shift):
            return chr((ord(c)- shift) % 26 + ord('a'))
        def getHash(s):
            shift = ord(s[0])
            return ''.join(shift_letter(c, shift) for c in s)
        
        dic = defaultdict(list)
        for s in strings:
            hashKey = getHash(s)
            dic[hashKey].append(s)
        
        return dic.values()