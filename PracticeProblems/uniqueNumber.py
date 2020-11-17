class Solution():
    def unique(self,nums):
        num = 0
        for x in nums:
            num = num ^ x
        return num

print(Solution().unique([1,2,3,4,4,3,1]))
