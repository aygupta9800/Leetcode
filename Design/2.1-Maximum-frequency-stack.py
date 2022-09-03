# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 


import collections

class FreqStack:

    def __init__(self):
        # mapping elem with its freq
        self.freqMap = collections.Counter()
        
        # mapping freq with list of elem in order
        self.groupByFreq = collections.defaultdict(list)
        
        # keeping track of max freq
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        # update val freq in freq map and put elem in new freq list
        # also dont forget to update max freq if needed
        f = self.freqMap[val] + 1
        self.freqMap[val] = f
        
        self.groupByFreq[f].append(val)
        
        if f > self.maxFreq:
            self.maxFreq = f
        
        

    def pop(self) -> int:
        # pop max freq elem which is last in list
        # update fre of that elem
        # then if max freq is change, update it
        elem = self.groupByFreq[self.maxFreq].pop()
        self.freqMap[elem] -= 1
        
        if len(self.groupByFreq[self.maxFreq]) == 0:
            # since the pop elem will have one less freq
            # so next max freq will be one less
            self.maxFreq -= 1
        return elem
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()