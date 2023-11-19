""" 322. Coin Change
Solved
Medium
Topics
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,5,7], amount = 11
11-1,11-5,11-7
10,6,4 (1,2,3)
(10-1,10-5,10-7) (6-1,6-5)(4-1)
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0 """

def CoinChange(coins,amount):

    memo = [float('inf')] * (amount+1)

    memo[0] = 0

    for coin in coins:
        for amt in range(coin,amount+1):
            memo[amt] = min(memo[amt],memo[amt-coin]+1)
            print(coin,amt)
            print(memo)

    return memo[amount] if memo[amount] != float('inf') else -1

print(CoinChange([1,2,5],11))

print(CoinChange([2],1))




