class Solution():
    def isValid(self,testString):
        pmap = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        revmap = {c:v for v,c in pmap.items()}
        stack = []

        for char in testString:
            if char in pmap:
                stack.append(char)
            elif char in revmap and stack.pop() != revmap[char] :
                return False
        
        if len(stack) == 0 :
            return True
        else: return False

print(Solution().isValid("([{}])"))
print(Solution().isValid("((([{}])"))



