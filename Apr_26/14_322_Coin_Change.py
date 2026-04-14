class Solution(object):
    def coinChange(self, coins, amount):
        memo = [-1] * (amount + 1)
        def solve(amt):
            if amt == 0:
                return 0
            if memo[amt] == -1:
                res = float('inf')
                for coin in coins:
                    if amt >= coin:
                        res = min(res, 1 + solve(amt - coin))
                memo[amt] = res
            return memo[amt]
        ans = solve(amount)
        return -1 if ans == float('inf') else ans

print(Solution().coinChange(coins = [1,2,5], amount = 11))