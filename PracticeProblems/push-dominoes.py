class Solution():
    def pushdom(self,dominoes):
        maxForce = len(dominoes)
        forces = [0]*len(dominoes)
        force = 0

        for i,d in enumerate(dominoes):
            if d == 'R' : 
                force = maxForce
            elif d == 'L':
                force = 0
            if force > 0 :
                forces[i] = force - 1
                force -= 1
        print(forces)
        force = 0
        for x in range(len(dominoes)-1,-1,-1):
            if dominoes[x] == 'L' : 
                force = maxForce
            elif dominoes[x] == 'R':
                force = 0
            if force > 0 :
                forces[x] -= force - 1
                force -= 1
        
        print(forces)

Solution().pushdom('..R...L..R.')
            

