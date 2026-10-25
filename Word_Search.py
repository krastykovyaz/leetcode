# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

# Example 1:
# Input: 
board = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ]
word = "CAT"

# Output: true
# Example 2:

# Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "BAT"

# Output: false

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[0] * cols for r in range(rows)]

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if board[r][c] != word[idx] or visited[r][c] == 1 or r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            visited[r][c] = 1
            found = dfs(r - 1, c, idx +1 ) or dfs(r + 1, c, idx +1 ) or dfs(r , c- 1, idx +1 ) or dfs(r , c+ 1, idx +1 )
            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c , 0):
                    return True
        return False



if __name__ == '__main__':
    s = Solution()
    
    print(s.exist(board, word))
