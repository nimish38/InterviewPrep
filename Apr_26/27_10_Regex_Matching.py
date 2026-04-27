class Solution(object):
    def isMatch(self, s, p):
        def solve(i, j):
            if i == len(s) and j == len(p):
                return True
            if i == len(s) or j == len(p):
                return False
            if p[j] == '.' or (p[j] == s[i]):
                return solve(i + 1, j + 1)
            elif p[j] == '*':
                c, res, k = s[i], solve(i, j + 1), 1
                while i + k < len(s) and s[i + k] == c:
                    if solve(i + k, j + 1):
                        return True
                    k += 1
                return solve(i + k, j + 1)
            else:
                return solve(i, j + 1)

        return solve(0, 0)

print(Solution().isMatch(s = "aab", p = "c*a*b"))

