from collections import deque


class Solution(object):
    def isBipartite(self, graph):
        n, color, vis = len(graph), [-1] * len(graph), 1
        def DFS(value, c):
            st = deque([(value, c)])
            color[value] = c
            while st:
                node, col = st.popleft()
                for nei in graph[node]:
                    if color[nei] == col:
                        return False
                    if color[nei] == -1:
                        st.append((nei, 1 - col))
                        color[nei] = 1 - col
            return True

        for v in range(n):
            if color[v] == -1:
                if not DFS(v, 1):
                    return False
        return True

print(Solution().isBipartite(graph = [[1,3],[0,2],[1,3],[0,2]]))

