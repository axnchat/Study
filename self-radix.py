from random import randrange

def quick_sort(list,start,end):
    if start >= end:
        return
    
    pivotIndx = randrange(start,end+1)

    pivot = list[pivotIndx]
    list[pivotIndx],list[end] = list[end],list[pivotIndx]

    less_than = start
    for idx in range(start,end):
        if pivot > list[idx]:
            list[less_than],list[idx] = list[idx],list[less_than]
            less_than += 1
    
    list[end],list[less_than] = list[less_than],list[end]
    left_sort = quick_sort(list,start,less_than-1)
    right_sort = quick_sort(list,less_than+1,end)

    return



def radix_sort(list):
    maxNum = max(list)
    max_num_str = str(maxNum)
    number_of_elements = len(max_num_str)    

    numbers_to_sort = list.copy()

    for x in range(1,number_of_elements+1):

        digits = [[] for x in range(10)]

        for number in numbers_to_sort:
            try:
                lastDigit = int(str(number)[-x])
                digits[lastDigit].append(number) 
            except:
                digits[0].append(number)

        numbers_to_sort = []
        for digit in digits:
            numbers_to_sort.extend(digit)

    return numbers_to_sort


unsorted_list = [170, 45, 75, 90, 802, 24, 2, 66]
#sorted_list = radix_sort(unsorted_list)
quick_sort(unsorted_list,0,len(unsorted_list)-1)
print(unsorted_list) 




    