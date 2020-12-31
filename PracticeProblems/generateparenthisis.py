class Solution():
    def generateParenth(self,count):
        string = ''
        result = self.mygenerateparenth(count,0,0,string)
        return result

    def mygenerateparenth(self,count,left,right,str):
        if left + right == 2*count:
            return [str]
        result = []
        if left < count:
            result += self.mygenerateparenth(count,left+1,right,str+'(')
        if right < left :
            result += self.mygenerateparenth(count,left,right+1,str+')')
        
        return result

print(Solution().generateParenth(3))