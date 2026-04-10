class Solution(object):
    def isBipartite(self, graph):
        n, color, st = len(graph), [-1] * len(graph), [(0, 1)]
        while st:
            node, col = st.pop()
            color[node] = col
            for nei in graph[node]:
                if color[nei] == col:
                    return False
                if color[nei] == -1:
                    st.append((nei, 1 - col))
        return True



