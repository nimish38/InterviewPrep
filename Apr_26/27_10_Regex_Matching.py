class Solution(object):
    def isMatch(self, s, p):
        def solve(i, j):
            if j >= len(p):
                if i >= len(s):
                    return True
                return False
            if j + 1 < len(p) and p[j + 1] == '*':
                take = False
                if i < len(s) and (p[j] == '.' or p[j] == s[i]):
                    take = solve(i + 1, j)
                skip = solve(i, j + 2)
                return take or skip
            else:
                if i < len(s) and (p[j] == '.' or p[j] == s[i]):
                    return solve(i + 1, j + 1)
                return False

        return solve(0, 0)

print(Solution().isMatch(s = "ab", p = ".*"))

