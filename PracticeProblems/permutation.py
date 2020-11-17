class Solution():
    def _permuhelp(self,nums,start=0):
        if len(nums) == 1:
            return nums[:]
        
        for i in range(0,len(nums)):
            return nums[i] + self._permuhelp(nums[0:i-1]+nums[i+1:])


