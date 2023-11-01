def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    visited = [ [False] * len(matrix[0]) for _ in range(len(matrix))]

    def bfs(x,y):
    
        directions = [(-1, 0),(0, -1),(1, 0),(-1, -1),(1, 1),(-1, 1),(1, -1),(0, 1)]
        
        myQ =[(x,y)]
        
        while myQ:
            x,y = myQ.pop(0)
            visited[x][y] = True
            for m,n in directions:
                if 0 <= x+m <= (len(matrix) -1) and 0<= y+n <= (len(matrix[0]) -1) and matrix[x+m][y+n] == 1 and visited[x+m][y+n] == False:
                    myQ.append((x+m,y+n))
        
        return


    islands = 0
    
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 1 and visited[x][y] == False:
                islands +=1
                bfs(x,y)
    
    print(visited)
    return islands

matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]
print(count_islands(matrix))