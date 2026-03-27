class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        memo = [[-1] * n for _ in range(m)]
        def solve(i, j):
            if i == m or j == n:
                return 0
            if memo[i][j] == -1:
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + solve(i + 1, j + 1)
                else:
                    memo[i][j] = max(solve(i + 1, j), solve(i, j + 1))
            return memo[i][j]
        return solve(0, 0)

print(Solution().longestCommonSubsequence(text1 = "abc", text2 = "def" ))