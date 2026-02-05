class Solution(object):
    def minPathSum(self, grid):
        m, n, memo = len(grid), len(grid[0]), []
        for i in range(m):
            row, val = [], -1
            for j in range(n):
                if i == 0 and j == 0:
                    val = grid[i][j]
                elif i == 0:
                    val = grid[i][j] + row[j - 1]
                elif j == 0:
                    val = grid[i][j] + memo[i - 1][j]
                else:
                    val = grid[i][j] + min(row[j - 1], memo[i - 1][j])
                row.append(val)
            memo.append(row)
        return memo[-1][-1]
                    

print(Solution().minPathSum(grid = [[1,2,3],[4,5,6]]))