mylist = [1, 3, 4, 5, 7, 9, 13, 15, 16, 17, 19]


# mylist = [1,3,4,5,7,9]
def binSearch(arr, start, end, num):
    print("start:" + str(start))
    print("end:" + str(end))
    print("num:" + str(num))

    mid = int((end + start) / 2)
    print("mid:" + str(mid))
    print("indexNum:" + str(arr[mid]))
    if (arr[mid] == num):
        print("Found:" + str(arr[mid]))
        return
    if (mid == start) | (mid == end):
        print("NotFound:")
        return
    elif arr[mid] > num:
        binSearch(arr, start, mid, num)
    else:
        binSearch(arr, mid, end, num)


binSearch(mylist, 0, len(mylist) - 1, 15)
