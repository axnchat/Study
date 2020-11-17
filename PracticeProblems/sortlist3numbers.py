class Solution():
    def sort_three(self,mylist):
        one_idx = 0
        three_idx = len(mylist)-1
        idx = 0
        while idx <= three_idx:
            if mylist[idx] == 1:
                mylist[idx],mylist[one_idx] = mylist[one_idx],mylist[idx]
                one_idx += 1
                idx += 1
            elif mylist[idx] == 2 :
                idx += 1
            elif mylist[idx] == 3:
                mylist[idx],mylist[three_idx] = mylist[three_idx],mylist[idx]
                three_idx -= 1
        return mylist

print(Solution().sort_three([3,1,2,2,1,3,3,2,1,2,2,1,1]))
