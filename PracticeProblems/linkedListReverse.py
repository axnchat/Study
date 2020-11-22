class Node():
    def __init__(self,val,next=None):
        self.value = val
        self.next = next
    def printme(self):
        while(self):
            print(self.value)
            self = self.next

class Solution():
    def reverse(self,node) -> Node :
        if node:
            current = node.next
            node.next = None
        while(current):
            tmp = current.next
            current.next = node
            node = current
            current = tmp
        return node
            

fifth = Node(5)
fourth = Node(4,fifth)
third = Node(3,fourth)
second = Node(2,third)
top = Node(1,second)
top.printme()
Solution().reverse(top).printme()

