class Solution(object):
    def coinChange(self, coins, amount):
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                diff = i - coin
                if diff < 0:
                    break
                memo[i] = min(memo[i], 1 + memo[diff])
        return memo[amount] if memo[amount] != float('inf') else -1

print(Solution().coinChange(coins = [1,2,5], amount = 11))