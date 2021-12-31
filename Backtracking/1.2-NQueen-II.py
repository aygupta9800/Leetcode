# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals, antiDiagonals, cols):
            # Base case - N queens have been placed
            if row == n:
                return 1
            
            solutions  =0
            for col in range(n):
                curDiagonal = row -col
                curAntiDiagonal = row + col
                # If the queen is not placeable
                if (col in cols or curDiagonal in diagonals or
                    curAntiDiagonal in antiDiagonals):
                    continue
                
                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curDiagonal)
                antiDiagonals.add(curAntiDiagonal)
                
                # Move on the next row with the updated board state
                solutions += backtrack(row+1, diagonals, antiDiagonals, cols)
                
                #Remove the queen from the board since we have already explored all valid path
                cols.remove(col)
                diagonals.remove(curDiagonal)
                antiDiagonals.remove(curAntiDiagonal)
                
            return solutions
        
        return backtrack(0, set(), set(), set())