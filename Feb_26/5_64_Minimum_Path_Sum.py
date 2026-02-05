class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        memo = [[-1]* n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    memo[i][j] = grid[i][j]
                elif i == 0:
                    memo[i][j] = grid[i][j] + memo[i][j - 1]
                elif j == 0:
                    memo[i][j] = grid[i][j] + memo[i - 1][j]
                else:
                    memo[i][j] = grid[i][j] + min(memo[i][j - 1], memo[i - 1][j])
        return memo[-1][-1]
                    

print(Solution().minPathSum(grid = [[1,2,3],[4,5,6]]))