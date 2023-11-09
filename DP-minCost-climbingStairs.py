""" 746. Min Cost Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6. """

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) < 3:
            return min(cost)

        memo = [float('inf') for _ in range(len(cost))]
        #print(cost)
        #print(memo)
        memo[0] = cost[0]
        memo[1] = cost[1]
        for i in range(2,len(cost)):
            memo[i] = min(memo[i-1],memo[i-2]) + cost[i]
            #print(memo)

        return min(memo[-1],memo[-2])
        