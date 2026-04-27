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
                c, res, k = s[i], False, 0
                while i + k < len(s) and s[i + k] == c:
                    if solve(i + k, j + 1):
                        return True
                return False
            else:
                return False

        return solve(0, 0)

