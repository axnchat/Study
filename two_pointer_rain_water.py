""" 42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9 """
 

class Solution:
    def trap(self, height: list[int]) -> int:
        total_water = 0
        left_pointer = 0
        right_pointer = len(height)-1
        left_bound = 0
        right_bound = 0
        while left_pointer < right_pointer:
            if height[left_pointer] <= height[right_pointer]:
                left_bound = max(left_bound,height[left_pointer])
                total_water += left_bound - height[left_pointer]
                left_pointer += 1
            else:
                right_bound = max(right_bound,height[right_pointer])
                total_water += right_bound - height[right_pointer]
                right_pointer -= 1

        return total_water
    
sol = Solution()

print(sol.trap([4,2,0,3,2,5]))
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))