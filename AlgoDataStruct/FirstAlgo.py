import numpy as np
import math
mylist = [4,9,7,1,3,6,5]
#print(*mylist)
def sortlinear() :
    x = 0
    y = 1
    minIndex = 0
    min = math.inf
    for i in mylist[x:-2]:
       for j in mylist[x+1:]:
           if(j < min):
               min = j
               minIndex = y
               print(min)
           y = y+1
       print("min:" + str(min))
       print("minIndex:" + str(minIndex))
       if(min < i):
           tmp = mylist[x]
           mylist[x] = mylist[minIndex]
           mylist[minIndex] = tmp
    x = x+1
    min = math.inf
    minIndex = y
    y= x+1
    print(*mylist)

def selectionsort(arr):
    x=0
    y=0
    min = math.inf
    minindex = math.inf
    for x in range(len(arr)-1):
        for y in range(x+1,len(arr)):
            if(arr[y] < min):
                min = arr[y]
                minindex = y
        if(arr[x]>min):
            arr[minindex]=arr[x]
            arr[x]=min
        min = math.inf
        minindex = math.inf
    print(*arr)


def bubbleSort(arr):
    i = 0
    j = 0
    swap = 0
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if (arr[j] < arr[j-1]):
                swap = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = swap
    print(*arr)
def combineSort(arr,start,mid,end):
        temp = [0]*(end-start+1)
        i=0
        for x in arr[start:mid]:
            for y in arr[mid:end]:
                if(i<(end-start)):
                    if(y<x):
                        temp[i]=y
                        i = i + 1
                    else:
                        temp[i]=x
                        i = i + 1
                        break
                else: break
        arr[start:end]=temp[start:end]
        return arr




def mergeSort(arr,start,end):
    if((end-start)<2):
        print(arr[start:end])
        return arr[start:end]
    elif((end-start)==2):
        if(arr[0]>arr[1]):
            temp=arr[0]
            arr[0]=arr[1]
            arr[1]=temp
        print(arr[start:end])
        return arr[start:end]
    else:
        mid=int((start+end)/2)
        mergeSort(arr,start,mid)
        mergeSort(arr,mid,end)
    print(arr[start:end])
    return combineSort(arr,start,mid,end)





#print(*mylist)
#selectionsort(mylist)
print(*mylist)
#bubbleSort(mylist)
mergeSort(mylist,0,len(mylist)-1)
print(*mylist)








