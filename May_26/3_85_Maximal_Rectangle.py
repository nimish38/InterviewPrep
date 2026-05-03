class Solution(object):
    def maximalRectangle(self, matrix):
        m, n = len(matrix), len(matrix[0])
        row = matrix[0].copy()

        def getNSE(row):
            st, arr = [], [n] * n
            for i in range(n - 1, -1, -1):
                if st:
                    arr[i] = st[-1]
                while st and row[i] <= row[st[-1]]:
                    st.pop()
                st.append(i)
            return arr

        def getPSE(row):
            st, arr = [], [-1] * n
            for i in range(n):
                if st:
                    arr[i] = st[-1]
                while st and row[i] <= row[st[-1]]:
                    st.pop()
                st.append(i)
            return arr

        def getMaxArea(row):
            nse, pse, curr = getNSE(row), getPSE(row), 0
            for i in range(n):
                curr = max(curr, row[i] * (nse[i] - pse[i] - 1))
            return curr

        area = getMaxArea(row)
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c]:
                    row[c] += 1
                else:
                    row[c] = 0
            area = max(area, getMaxArea(row))
        return area