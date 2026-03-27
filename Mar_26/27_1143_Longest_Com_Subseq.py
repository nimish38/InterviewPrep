class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        def solve(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + solve(i + 1, j + 1)
            return max(solve(i + 1, j), solve(i, j + 1))
        return solve(0, 0)