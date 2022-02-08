# https://leetcode.com/problems/design-tic-tac-toe/

# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.


class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0 for r in range(n)]
        self.cols = [0 for c in range(n)]
        self.diagonal = 0
        self.antiDiagonal = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        currentPlayer = 1 if player == 1 else -1
        # update currentplayer in rows and cols arrays
        self.rows[row] += currentPlayer
        self.cols[col] += currentPlayer
        # // update diagonal
        if row == col:
            self.diagonal += currentPlayer
        if row+ col == self.n-1:
            self.antiDiagonal += currentPlayer
        
        # check if current player wins
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n \
        or abs(self.diagonal) == self.n or abs(self.antiDiagonal) == self.n:
            return player
        # No one wins
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)