class Solution():
    def missingPos(self,array):
        mysum = 0
        mymax = float("-inf")
        for x in array:
            if x > 0:
                mysum += x
                mymax = max(x,mymax)

        return int(mymax*(mymax+1)/2) - mysum
print(Solution().missingPos([-1,1,3,4]))
                
