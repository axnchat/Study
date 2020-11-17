class Node():
    def __init__(self,val):
        self.value = val
        self.next = None
class Solution():
    def addTwoLL(self,l1,l2):
        a = l1
        b = l2
        carry = 0
        firstsuml = suml = None
        while a or b :
            if not a :
                a = Node(0)
            if not b :
                b = Node(0)
            if not suml :
                firstsuml = suml = Node(int((a.value + b.value + carry)%10))
            else :
                suml.next = Node(int((a.value + b.value + carry)%10))
                suml = suml.next
            carry = int((a.value + b.value + carry)/10)
            a = a.next
            b = b.next
        if carry > 0:
            suml.next = Node(carry)

        while firstsuml:
            print(firstsuml.value)
            firstsuml = firstsuml.next

        return

first = Node(1)
first.next = Node(2)
first.next.next = Node(7)

second = Node(2)
second.next = Node(3)
second.next.next = Node(3)
Solution().addTwoLL(first,second)
    

        
        
            

