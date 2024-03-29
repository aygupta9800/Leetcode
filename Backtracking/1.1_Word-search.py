
# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically
# neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Approach 2
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # updated soln: instead of visit set, mark the node with sth and remove mark before return

        m, n = len(board), len(board[0])
        
        def backtrack(r, c, i):
            #base case

            if len(word) == i:
                return True

            #Check if current state valid
            if r < 0 or r == m or c <0 or c == n or board[r][c] != word[i]:
                return False

            #Mark the choice before exploring
            board[r][c] = "#"
            for row, col in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                if backtrack(row, col, i+1):
                    return True
            board[r][c] = word[i]
            # return res
            return False
        
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
                
        return False
    


# Approach 1:(backtrack with visit set)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        # i is index of word from where we have to match
        def dfs(r, c, i):
            if i == len(word):
                return True
            # Instead of doing the boundary checks before the recursive call on the backtrack() function, we do               it within the function so to reach bottom case for the test case where the board contains only a               single cell, since either of neighbor indices would not be valid.
            # check boundary or if in visit or first word is same as curr value
            #this check is not called when calling for nei but here so to
            if r<0 or c<0 or r>= ROWS or c>= COLS or word[i] != board[r][c] or (r,c) in visit:
                return False
            visit.add((r,c))
            lst = [(r+1,c, i+1), (r-1,c, i+1), (r,c+1, i+1), (r,c-1, i+1)]
            
            res = False
            for row, col, index in lst:
                if dfs(row, col, index):
                    res = True
                    break
            
            visit.remove((r,c))
            return res
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False
        
        
    