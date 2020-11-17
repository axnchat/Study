class Solution():
    def twoSum(self,items,sm):
        mymap = {}
        idx = 0
        for item in items :
            if sm-item in mymap :
                return (idx,mymap[sm-item])
            else:
                mymap[item] = idx
            idx += 1
        return(-1,-1)

print(Solution().twoSum([1,2,3,5],8))

