class Solution(object):
    def numDistinct(self, s, t):
        memo = [[-1] * len(t) for _ in range(len(s))]
        def solve(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if memo[i][j] == -1:
                memo[i][j] = 0
                if s[i] == t[j]:
                    memo[i][j] += solve(i + 1, j + 1)
                memo[i][j] += solve(i + 1, j)
            return memo[i][j]
        return solve(0, 0)

print(Solution().numDistinct(s = "babgbag", t = "bag"))