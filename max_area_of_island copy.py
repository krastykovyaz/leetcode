# Max Area of Island
# Medium
# Topics
# Company Tags
# Hints
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

# Example 1:

# Input: 
grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

# Output: 6
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_island = 0
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return (1 + 
            dfs(r + 1, c ) + 
            dfs(r - 1, c ) + 
            dfs(r, c + 1 ) + 
            dfs(r, c - 1)
            )
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    out = dfs(r,c)
                    max_island = max(out, max_island)
        return max_island

if __name__ =='__main__':
    s = Solution()
    print(s.maxAreaOfIsland(grid))