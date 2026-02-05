class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        memo = [[0]* n for _ in range(m)]
        memo[0][0] = grid[0][0]

        def solve(i, j):
            if i == 0 and j == 0:
                return memo[i][j]
            up, left = float('inf'), float('inf')
            if i > 0:
                up = solve(i - 1, j)
            if j > 0:
                left = solve(i, j - 1)
            memo[i][j] = grid[i][j] + min(up, left)
            return memo[i][j]

        return solve(m - 1, n - 1)