# ex.
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

# Approach 1 Using Heap Nlogk time , o(n) space
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        arr = [(-cnt, w) for w, cnt in counter.items()]
        arr = heapq.nsmallest(k, arr, key= lambda x: (x[0], x[1]))
        res = [x[1] for x in arr]
        return res

# Approach 3 Using heap , but with custom sort logic
from heapq import heappush, heappop, heappushpop

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapper = defaultdict(int)
        for word in words:
            mapper[word] += 1
        
        h = list()
        for word, freq in mapper.items():
            node = Node(word, freq)
            if len(h) == k:
                heappushpop(h, node)
            else:
                heappush(h, node)
                
        result = list()
        while h:
            result.append(heappop(h).word)
        return result[::-1]

#Approch2: Nlogn basic sorting
def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # dict = defaultdict(int)
        # for x in words:
        #     dict[x] += 1
        dict = Counter(words)
        res = sorted(dict, key=lambda x: (-dict[x], x))
        return res[:k]