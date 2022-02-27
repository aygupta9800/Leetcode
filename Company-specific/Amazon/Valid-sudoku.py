# TIme O(9*9) 9= board len
# SPace O(9*9)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(9)]
        rows = [set() for j in range(9)]
        #can use single array r//3 * 3+ c//3
        squares = [[set() for i in range(3)] for j in range(3)] #key(r//3, c//3)

        for r in range(9):
            for c in range(9):
                curVal = board[r][c]
                if curVal == '.':
                    continue
                if curVal in cols[c] or curVal in rows[r] or curVal in squares[r//3][c//3]:
                    return False
                cols[c].add(curVal)
                rows[r].add(curVal)
                squares[r//3][c//3].add(curVal)
        return True
        