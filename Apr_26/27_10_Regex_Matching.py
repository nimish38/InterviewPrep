class Solution(object):
    def isMatch(self, s, p):
        memo = [[-1] * (len(s) + 1) for _ in range(len(p) + 1)]
        def solve(i, j):
            if j >= len(p):
                if i >= len(s):
                    return True
                return False
            if memo[i][j] == -1:
                if j + 1 < len(p) and p[j + 1] == '*':
                    take = False
                    if i < len(s) and (p[j] == '.' or p[j] == s[i]):
                        take = solve(i + 1, j)
                    skip = solve(i, j + 2)
                    memo[i][j] = take or skip
                else:
                    if i < len(s) and (p[j] == '.' or p[j] == s[i]):
                        memo[i][j] = solve(i + 1, j + 1)
                    else:
                        memo[i][j] = False
            return memo[i][j]

        return solve(0, 0)

print(Solution().isMatch(s = "ab", p = ".*"))

