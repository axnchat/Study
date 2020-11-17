class Solution():
    def intersect_two_sorted(self,A,B):
        indxA = 0
        indxB = 0
        common = []
        while indxA < len(A) and indxB < len(B) :
            if A[indxA] < B[indxB]:
                indxA += 1
            elif A[indxA] == B[indxB] :
                if A[indxA] not in common :
                    common += [A[indxA]]
                indxA += 1
                indxB += 1
            else :
                indxB += 1
        return common
print(Solution().intersect_two_sorted([2,3,3,5,5,6,7,7,8,12],[5,5,6,8,8,9,10,10]))



