class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        def solve(i):
            if i == 1:
                return x
            if i % 2:
                return x * solve(i // 2) * solve( i // 2)
            return solve(i // 2) * solve( i // 2)
        return solve(n)

print(Solution().myPow(x = 2.10000, n = 3))