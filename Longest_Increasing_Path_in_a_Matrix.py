# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

matrix = [[9,9,4],[6,6,8],[2,1,1]]

def find_path(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    cache = [[0] * n for _ in range(m)]
    def dfs(r, c):
        if cache[r][c] != 0:
            return cache[r][c]
        best = 1
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))
        cache[r][c] = best
        return best
    longest = 0
    for r in range(m):
        for c in range(n):
            longest = max(longest, dfs(r, c))
    return longest
            

if __name__=='__main__':
    print(find_path(matrix))
