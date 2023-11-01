#https://leetcode.com/problems/pacific-atlantic-water-flow/
""" There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans. """



class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(heights), len(heights[0])
        result = []

        
        pacificOcean = [ [False] * n for _ in range(m) ]
        atlanticOcean = [ [False] * n for _ in range(m)]

        def dfs(x,y,whichOcean):
            whichOcean[x][y] = True
            for i,j in directions:
                if 0 <= x+i < m and 0 <= y+j < n and heights[x+i][y+j] >= heights[x][y] and not whichOcean[x+i][y+j]:
                    dfs(x+i,y+j,whichOcean)

        for i in range(n):
            dfs(0,i,pacificOcean)
        for j in range(m):
            dfs(j,0,pacificOcean)

        for i in range(n):
            dfs(m-1,i,atlanticOcean)
        for j in range(m):
            dfs(j,n-1,atlanticOcean)


        
        
        
        for i in range(m):
            for j in range(n):
                if pacificOcean[i][j] and atlanticOcean[i][j]:
                    result.append([i,j])
        
        return result
    
solution = Solution()

# Test 1
heights1 = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
result1 = solution.pacificAtlantic(heights1)
# Expected Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
print(result1)

# Test 2
heights2 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
result2 = solution.pacificAtlantic(heights2)
# Expected Output: [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
print(result2)

