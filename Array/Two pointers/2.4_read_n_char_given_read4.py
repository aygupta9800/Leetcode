# Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.
# Method read4:
# The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.
# The return value is the number of actual characters read.
# Definition of read4:
#     Parameter:  char[] buf4
#     Returns:    int
# buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

#soln 1 Using internal buffer of 4 characeters
# TIme O(n) to copy N characters
# space O(1) for 4 char

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copied_chars = 0
        read_chars = 4
        buf4 = [""] * 4
        while copied_chars <n and read_chars == 4:
            read_chars = read4(buf4)
            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars +=1
        return copied_chars