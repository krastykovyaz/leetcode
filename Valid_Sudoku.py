# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Input: 
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

# Output: true

# Example 2:

# Input: 
# board = [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

def is_sudoku_valid(board):
    if not any(board):
        return False
    columns = [set() for _ in range(9)]
    rows = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == ".":
                continue
            box = (i // 3)  + (j // 3) * 3
            if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in boxes[box]:
                return False
            boxes[box].add(board[i][j])
            columns[j].add(board[i][j])
            rows[i].add(board[i][j])
    return True


        

    

if __name__=='__main__':
    print(is_sudoku_valid(board))