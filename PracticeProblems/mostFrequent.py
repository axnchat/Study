import heapq
import collections
class Solution():
    def mostfreq(self,myarray,topx):
        mymap = collections.defaultdict(int)
        for idx in myarray:
            mymap[idx] += 1
        
        heap = []
        for num, c in mymap.items():
            heap.append((-c, num))
        heapq.heapify(heap)

        print(heap)
        result = []
        for i in range(topx):
            result.append(heapq.heappop(heap)[1])
        return result



print(Solution().mostfreq([1,1,1,1,2,2,3], 2))