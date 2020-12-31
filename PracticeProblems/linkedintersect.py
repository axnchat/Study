class Node():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class Solution():
    def intersect(self,N1,N2):
        first = N1
        second = N2
        flag = False
        while first.val != second.val :
            #print(first.val)
            #print(second.val)
            if flag:
                first = first.next
            else:
                second = second.next
            flag = not flag
            if not first or not second:
                return -1
        return first.val

N1= Node(1,Node(3,Node(2,None)))
N2= Node(4,Node(2,Node(5,None)))
print(Solution().intersect(N1,N2))
