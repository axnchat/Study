myMap = {")":"(","]":"[","}":"{"}
myClosing = (")","}","]")
def matching_parenthesis(expr):
    myStack = []
    for char in expr:
        if char in myClosing:
            if len(myStack) == 0 or myMap[char] != myStack.pop():
                return False
        else:
            myStack.append(char)
    
    if len(myStack) > 0:
        return False
    
    return True

            
print(matching_parenthesis("()[]{}"))
print(matching_parenthesis("()]{}"))
print(matching_parenthesis("{[()]}"))
print(matching_parenthesis(""))