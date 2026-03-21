class Solution(object):
    def numIslands(self, grid):
        cnt, m, n = 0, len(grid), len(grid[0])
        def dfs(i, j):
            st = [(i, j)]
            grid[i][j] = 'v'
            nei = [(1, 0),(-1, 0), (0, 1), (0, -1)]
            while st:
                p, q = st.pop()
                for x, y in nei:
                    dx, dy = p + x, q + y
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == '1':
                        st.append((dx, dy))
                        grid[dx][dy] = 'v'
        for k in range(m):
            for l in range(n):
                if grid[k][l] == '1':
                    dfs(k, l)
                    cnt += 1
        return cnt

print(Solution().numIslands( grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))