# You are given a 
# m
# ×
# n
# m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        rows = len(grid)
        cols = len(grid[0])
        q = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        while q:
            r, c = q.pop(0)
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))


if __name__=='__main__':
    s = Solution()
    grid = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]
    s.islandsAndTreasure(grid)
    print(grid)

        