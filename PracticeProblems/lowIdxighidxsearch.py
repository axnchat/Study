class Solution():
    def searchList(mylist,number):
        low = binsearch(mylist,number,idxL,idxH,True)
        high = binSearch(mylist,number,idxL,idxH, False)
        return(low,high)
    def binsearch(mylist,number,Low,High,findLow):
        mid = Low + int((High - Low)/2)
        low,high = Low,High
        retlow,rethigh = -1,-1
        if findLow:
            while mylist[mid] != number  or mylist[mid-1] == number :
                if mylist[mid] >= number:
                    high = mid
                else:
                    low = mid
                mid = low + int((high - low)/2)
            if mid == 0 and mylist[mid] != number :
                return -1
            else:
                return mid
        else:
            while mylist[mid] != number  or mylist[mid+1] == number :
                if mylist[mid] <= number:
                    low = mid
                else:
                    high = mid
                mid = low + int((high - low)/2)
            if mid == High and mylist[mid] != number :
                return -1
            else:
                return mid
        



