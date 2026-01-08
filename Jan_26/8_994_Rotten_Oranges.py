from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        m, n, time, fresh, st = len(grid), len(grid[0]), 0, 0, deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    st.append((i, j))

        while st:
            for _ in range(len(st)):
                a, b = st.popleft()
                nei = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for x, y in nei:
                    p, q = a + x, b + y
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == 1:
                        fresh -= 1
                        st.append((p, q))

        return time if fresh == 0 else -1
