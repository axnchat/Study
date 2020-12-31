class Node():
    def __init__(self,value=0,next = None):
        self.val = value 
        self.next = next

    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def mymerge(node1,node2):
    one = node1
    two = node2
    top = Node()
    merged = top
    
    while one and two:
        print(top)
        if one.val < two.val:
            merged.next = one 
            one = one.next
        else: 
            merged.next = two
            two = two.next
        merged = merged.next
        
    if one:
        merged.next = one
    else:
        merged.next = two
    return top#.next


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

print(a)
# 135
print(b)
# 246
print(mymerge(a, b))
# 123456


