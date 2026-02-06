class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        memo = [[-1] * n for _ in range(m)]
        def solve(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if memo[i][j] == -1:
                if word1[i] == word2[j]:
                    memo[i][j] = solve(i + 1, j + 1)
                else:
                    ins = solve(i, j + 1)
                    dele = solve(i + 1, j)
                    rep = solve(i + 1, j + 1)
                    memo[i][j] = 1 + min(ins, dele, rep)
            return memo[i][j]
        return solve(0, 0)

print(Solution().minDistance(word1 = "intention", word2 = "execution"))