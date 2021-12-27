# read-n-characters-given-read4-ii-call-multiple-times
# Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

# Read characters from file into internal buffer self.buf4, store number of characters in the internal buffer in self.n4, keep track of current internal buffer position in self.i4. For each read call - use local var i to keep track of the number of copied characters, while it's less than n copy charaters from the internal buffer into the output buffer at the positions self.i4 and i respectively and increment both positions. If self.i4 becomes equal to self.n4 - we need to read another chunk from the file using read4, update self.n4, and reset self.i4 to 0. If self.n4 is 0 after read4 - there's no more data in the file, break out of the loop. Once loop is finished - return i which is the number of actually copied characters.

#TIme O(n)
#space o(1)

class Solution:
    def __init__(self):
        self.buf4 = [""] * 4
        self.i4 = 0
        self.n4 = 0
        
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.i4 == self.n4:
                self.i4  = 0
                self.n4 = read4(self.buf4)
                if self.n4 == 0:
                    break
            buf[i] = self.buf4[self.i4]
            self.i4 += 1
            i += 1
        return i  