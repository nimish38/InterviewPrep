class Solution(object):
    def floodFill(self, image, sr, sc, color):
        m, n, st, origin = len(image), len(image[0]), [], -1
        if image[sr][sc] != color:
            origin = image[sr][sc]
            st.append((sr, sc))
        nei = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while st:
            a, b = st.pop()
            image[a][b] = color
            for i, j in nei:
                x, y = a + i, b + j
                if 0 <= x < m and 0 <= y < n and image[x][y] == origin:
                    st.append((x, y))
        return image
