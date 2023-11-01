def max_island_size(grid):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def bfs(x, y):
        myQ = [(x, y)]
        size = 0  # Initialize the size to 0

        while myQ:
            m, n = myQ.pop()
            if visited[m][n]:
                continue
            visited[m][n] = True

            for a, b in directions:
                if 0 <= m + a < len(grid) and 0 <= n + b < len(grid[0]) and not visited[m + a][n + b] and grid[m + a][n + b] == 1:
                    myQ.append((m + a, n + b))
                    size += 1

        return size

    maxsize = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not visited[i][j]:
                maxsize = max(maxsize, bfs(i, j))

    return maxsize

grid = [
    [0, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 0]
]
print(max_island_size(grid))

