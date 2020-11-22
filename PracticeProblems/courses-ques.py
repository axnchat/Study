class Solution():
    def hasCycle(self,course,coursegraph,seen,cyclecache):
        if course in cyclecache :
            return cyclecache[course]
        ret = False
        if course in seen:
            return True
        if course not in coursegraph:
            return False
        else:
            seen.add(course)
            for x in coursegraph[course]:
                if self.hasCycle(x,coursegraph,seen,cyclecache) :
                    ret = True
                    break
                       
            seen.remove(course)
        
        cyclecache[course] = ret
        return ret



    def courses(self,countCourses,prereqs):
        courseGraph = {}
        for item in prereqs :
            if item[0] in courseGraph :
                courseGraph[item[0]].append(item[1])
            else:
                courseGraph[item[0]] = [item[1]]
        #print courseGraph

        cyclecache = {}
        for course in range(countCourses):
            if self.hasCycle(course,courseGraph,set(),cyclecache):
                return False
        return True
    
print(Solution().courses(2, [[1, 0]]))


print(Solution().courses(2, [[1, 0], [0, 1]]))





