# https://leetcode.com/problems/n-queens/

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

#Logic:
# 1. we create 3 sets for constraints on cols, diagonal and antidaigonals
# 2. we create a board of n* n with empty string "." 
# 3. in out backtracking fn backtrack(row)
    # a. we traverse col from 0 to n-1:
    #   place queen if valid , call backtrack, if not reset the state
    #   in base cond if row == n: append answer in correct format.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def create_board(board):
            output = []
            for row in board:
                output.append("".join(row))
            return output
        
        def backtrack(row, diagonals, antiDiagonals, cols, board):
            # Base case when we reach end of the rows
            if row == n:
                res.append(create_board(board))
                return
            for col in range(n):
                curDiagonal = row -col
                curAntiDiagonal = row +col
                # Check if we can place queen:
                if (curDiagonal in diagonals or curAntiDiagonal in antiDiagonals \
                   or   col in cols):
                    continue
                # Place queen
                cols.add(col)
                diagonals.add(curDiagonal)
                antiDiagonals.add(curAntiDiagonal)
                board[row][col] = "Q"
                
                #Move to next row
                backtrack(row+1, diagonals, antiDiagonals, cols, board)
                #backtrack
                board[row][col] = "."
                cols.remove(col)
                diagonals.remove(curDiagonal)
                antiDiagonals.remove(curAntiDiagonal)
                    
            
        res = []
        board = [["."] * n for _ in range(n)]
        # we keep three sets to keep track of col, diagonal, antidiagonal
        backtrack(0, set(), set(), set(), board)
        return res
        
        
