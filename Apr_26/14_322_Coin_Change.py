class Solution(object):
    def coinChange(self, coins, amount):
        def solve(amt):
            if amt == 0:
                return 0
            res = float('inf')
            for coin in coins:
                if amt >= coin:
                    res = min(res, 1 + solve(amt - coin))
            return res
        ans = solve(amount)
        return -1 if ans == float('inf') else ans

