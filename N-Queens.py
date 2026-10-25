# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.
# A queen in a chessboard can attack horizontally, vertically, and diagonally.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.
# You may return the answer in any order.

# Input: 
n = 4

# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There are two different solutions to the 4-queens puzzle.

# Example 2:

# Input: n = 1

# Output: [["Q"]]

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [['.'] * n for _ in range(n)]
        def backtrack(r):
            if n == r:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in cols or r - c in diag1 or r + c in diag2:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                
                backtrack(r + 1)
                board[r][c] = '.'
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return res

if __name__=='__main__':
    s = Solution()
    print(s.solveNQueens(n))

        