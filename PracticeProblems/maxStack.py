class MaxStack():
    def __init__(self):
        self.stack = []
        self.maxStack = []
    
    def push(self,value):
        self.stack.append(value)
        if self.maxStack and value < self.maxStack[-1] :
            self.maxStack.append(self.maxStack[-1])
        else:
            self.maxStack.append(value)
    
    def pop(self):        
        if self.maxStack:
            self.maxStack.pop()
        return self.stack.pop()

    #def __repr__

    def max(self):
        return self.maxStack[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
    