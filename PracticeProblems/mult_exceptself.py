class Solution():
    def multExceptSelf(self,myarray):
        leftProds = [1]* len(myarray)
        rightProds = [1]* len(myarray)

        for i in range(1,len(myarray)):
            leftProds[i] = leftProds[i-1]*myarray[i-1]
            rightProds[len(myarray)-i-1]  =  rightProds[len(myarray)-i]*myarray[len(myarray)-i]

        print(leftProds)
        print(rightProds)
        for i in range(0,len(myarray)):
            print(leftProds[i]*rightProds[i])
    
Solution().multExceptSelf([1,2,3,4])
