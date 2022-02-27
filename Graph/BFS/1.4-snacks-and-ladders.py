# O(n)
import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # O(n)
        board.reverse()

        def intToPos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r %2: # if r is odd
                c = n-1 - c
            return (r, c)

        q = collections.deque([[1, 0]]) # square ,moves
        visit = set()
        # O(n )
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == n*n:
                    return moves +1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1


        