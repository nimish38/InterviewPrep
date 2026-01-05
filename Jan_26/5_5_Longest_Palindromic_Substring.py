class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, self.length, self.res = len(s) - 1, 0, ''

        def expand(i, j):
            while i - 1 >= 0 and j + 1 <=n and s[i - 1] == s[j + 1]:
                i -= 1
                j += 1
            if (j - i + 1) > self.length:
                self.length = j - i + 1
                self.res = s[i: j + 1]

        for x in range(n + 1):
            expand(x, x)
            if x + 1 <= n and s[x] == s[x + 1]:
                expand(x, x + 1)
        return self.res


print(Solution().longestPalindrome(s = "cbbd"))