""" 213. House Robber II
Solved
Medium
Topics
Companies
Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000 """

class Solution:
    def rob1(self, nums: list[int]) -> int:
        memo = [ 0 for _ in range(len(nums))]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        
        memo[0] = nums[0]
        memo[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            memo[i] = max((memo[i-2] + nums[i]),memo[i-1])
        
        return max(memo[-1],memo[-2])
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        maxInc_zero = self.rob1(nums[0:len(nums)-1])
        maxInc_last = self.rob1(nums[1:len(nums)])
        return max(maxInc_zero,maxInc_last)