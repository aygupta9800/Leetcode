# https://leetcode.com/problems/sudoku-solver/
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Logic:
# 1. Constraint programming
#    a. create Data structure to store number in rows, colmn, boxes.
#    b. define logic to find box index
#    c. loop in sudoku and put given number in our DS.
# 2. Backtrack function for a given row, col:
#    a. define fun could_place(num, row, col)
#    b. define fun place_number(num, row, col)
#    c. define fun place_next_number(num, row, col)
#    d. define remove_number(num, row, col)
#    e. In backtrack fn loop through 1 to 9 and
#     check if could_place, then place_num, call place_next_num
#     and if sudoku not solved, remove_num
#    f. add base condn of last cell in place_next_num

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def place_number(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
            
        def place_next_number(row, col):
            """
            call backtrack fn in recursion to continue placing no.
            till the moment we have a soln
            """
            # if we are in last cell that means we have the soln
            if col == N -1 and row == N-1:
                nonlocal sudoku_solved
                sudoku_solved = True
            # if not yet
            else:
                # if we are in the end of the row:
                #go to the next row:
                if col == N-1:
                    backtrack(row+1, 0)
                else:
                    backtrack(row, col+1)
            
        def could_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or \
             d in boxes[box_index(row, col)])
        
        def remove_number(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = "."
        
        def backtrack(row = 0, col = 0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == ".":
                # iterate over all the numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        # calling backtrack for next cells
                        place_next_number(row, col)
                        # since the single soln is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_number(row, col)
                        
        
        #box size
        n = 3
        # row size
        N = n*n
        #lambda function to compute box index
        box_index = lambda row, col: (row // n) *n + col // n
        
        # init rows , columns and boxes for constraints
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for j in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        sudoku_solved = False
        backtrack()
                    
        