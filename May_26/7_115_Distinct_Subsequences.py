class Solution(object):
    def numDistinct(self, s, t):
        self.res = 0
        def solve(i, j):
            if j == len(t):
                self.res += 1
                return
            if i == len(s):
                return
            if s[i] == t[j]:
                solve(i + 1, j + 1)
            solve(i + 1, j)
        solve(0, 0)
        return self.res

print(Solution().numDistinct(s = "rabbbit", t = "rabbit"))