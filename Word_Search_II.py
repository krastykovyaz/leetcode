# Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

# For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

# Example 1:
# Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]

# Output: ["cat","back","backend"]

# Example 2:
# Input:
# board = [
#   ["x","o"],
#   ["x","o"]
# ],
# words = ["xoxo"]
# Output: []

class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def build_trie(self, words):
        root = Trie()
        for word in words:
            node = root
            for w in word:
                if w not in node.children:
                    node.children[w] = Trie()
                node = node.children[w]
            node.word = word
        return root
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.build_trie(words)
        res = []
        rows, cols = len(board), len(board[0])
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            board[r][c] = '#'
            for dr, dc in [(0, -1), (0, 1), (-1,0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#' :
                    dfs(nr, nc, next_node)
            board[r][c] = char
            # if not next_node.children:
            #     node.children.pop(char)



        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res
        

if __name__ == '__main__':
    s = Solution()
    print(s.findWords(board, words))
