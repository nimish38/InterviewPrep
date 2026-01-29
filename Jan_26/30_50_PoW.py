class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        memo = {}
        def solve(i):
            if i == 1:
                return x
            if i not in memo:
                if i % 2:
                    memo[i] = x * solve(i // 2) * solve( i // 2)
                else:
                    memo[i] =  solve(i // 2) * solve( i // 2)
            return memo[i]
        return solve(n)

print(Solution().myPow(x = 2.10000, n = 3))