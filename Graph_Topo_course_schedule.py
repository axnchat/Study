class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjList = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        
        for conn in prerequisites:
            adjList[conn[1]].append(conn[0])
        
        
        def dfs(item):
            visited[item] = 1
            
            for child in adjList[item]:
                if visited[child] == 0:
                    if not dfs(child): return False
                elif visited[child] == 1:
                    return False
            
            visited[item] = 2
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i) : return False
            
        return True
    
sol = Solution()
print(sol.canFinish(2,[[1,0],[0,1]]))