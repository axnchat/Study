class Solution():
    def queuerecontruction(self,input):
        input.sort(key=lambda x:
               (-x[0], x[1])
               )
        print(input)
        res = []
        for person in input:
            res.insert(person[1], person)
        return res


input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().queuerecontruction(input))