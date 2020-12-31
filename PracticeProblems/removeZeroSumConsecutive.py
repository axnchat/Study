import collections
class Solution():
    def removeZeroSumConsecut(self,thisarray):
        mymap = collections.OrderedDict()
        sum = 0
        lastidx = len(thisarray)-1
        for x in range(len(thisarray)):
            sum += thisarray[x]
            if sum in  mymap:
                lastidx = mymap[sum]
                break
            else:
                mymap[sum] = x
        print(lastidx)
        print(x)
        return thisarray[:lastidx+1] + thisarray[x+1:]

print(Solution().removeZeroSumConsecut([3, 1, 2, -1, -2, 4, 1]))





