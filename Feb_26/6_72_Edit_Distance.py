class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        def solve(i, j):
            if i == m:
                return n - j - 1
            if j == n:
                return m - i - 1
            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)
            ins = solve(i, j + 1)
            dele = solve(i + 1, j)
            rep = solve(i + 1, j + 1)
            return 1 + min(ins, dele, rep)
        return solve(0, 0)