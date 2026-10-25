grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6

def grid_search(grid):
    if not any(grid) or not grid[0]:
        return None
    
    around = [(0,1),(1,0),(0,-1),(-1,0)]
    max_area = 0
    m = len(grid)
    n = len(grid[0])
    visited = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and visited[i][j] != 1:
                stack = [(i,j)]
                visited[i][j] = True
                area = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for xd, yd in around:
                        xm = x + xd
                        ym = y + yd
                        if 0 <= xm < m and 0 <= ym < n:
                            if grid[xm][ym] == 1 and visited[xm][ym] != True:
                                visited[xm][ym] = True
                                stack.append((xm, ym))
                max_area = max(max_area, area)
    return max_area


if __name__=='__main__':
    print(grid_search(grid))
