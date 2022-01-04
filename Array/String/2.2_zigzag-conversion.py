
# Complexity Analysis
# Time Complexity: O(n)O(n), where n == \text{len}(s)n==len(s)
# Space Complexity: O(n)O(n)
#Approach : sort by row
# Intuition
# By iterating through the string from left to right, we can easily determine which row in the Zig-Zag pattern that a character belongs to.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        goingDown = False
        rows = [[] for i in range(numRows)]
        curRow = 0
        for i in range(0, len(s)):
            rows[curRow].append(s[i])
            if curRow == 0 or curRow == numRows -1:
                goingDown = not goingDown
            curRow +=  1 if goingDown else -1
        res = ""
        for i in range(numRows):
            res+= "".join(rows[i])
        return res


# Approach 2: Visit by Row
# Intuition

# Visit the characters in the same order as reading the Zig-Zag pattern line by line.

# Algorithm

# Visit all characters in row 0 first, then row 1, then row 2, and so on...

# For all whole numbers kk,

# Characters in row 00 are located at indexes k \; (2 \cdot \text{numRows} - 2)k(2⋅numRows−2)
# Characters in row \text{numRows}-1numRows−1 are located at indexes k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1k(2⋅numRows−2)+numRows−1
# Characters in inner row ii are located at indexes k \; (2 \cdot \text{numRows}-2)+ik(2⋅numRows−2)+i and (k+1)(2 \cdot \text{numRows}-2)- i(k+1)(2⋅numRows−2)−i.
