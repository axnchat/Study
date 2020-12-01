import random
class Solution():
    def kLargest(self,mylist,k):
        return self.largestinpart(mylist,0,len(mylist) - 1,len(mylist)-k)
    def largestinpart(self,mylist,start,end,idx):
        pivotIdx = random.randint(start,end)
        print("pivot:",mylist[pivotIdx])
        mylist[pivotIdx],mylist[end] =  mylist[end],mylist[pivotIdx]
        j = start
        for x in range(start,end) :
            if mylist[x] < mylist[end]:
                mylist[j],mylist[x] = mylist[x],mylist[j]
                j+=1
        mylist[end],mylist[j] = mylist[j],mylist[end]
        print("mylist:",mylist)
        if idx == j:
            return mylist[idx]
        if idx > j :
            return self.largestinpart(mylist,j+1,end,idx)
        else:
            return self.largestinpart(mylist,start,j-1,idx)


            

    
print(Solution().kLargest([3, 5, 2, 4, 6, 8], 6))