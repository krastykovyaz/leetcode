# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Example 1:



# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

# Output: 4
# Example 2:

# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

# Output: -1

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = []
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                iif grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        minutes = 0
        while queue and fresh:
            minutes += 1
            for _ in range(len(queue)):
                r,c = queue.pop(0)
                for dr, dc in [[1,0],[-1,0],[0,1], [0,-1]]:
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[[nr][nc]] = 2
                        minutes += 1
                        fresh -= 1
                        queue.append((nr, nc))
        return minutes if fresh == 0 else -1
