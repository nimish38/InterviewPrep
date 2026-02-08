class Solution(object):
    def largestRectangleArea(self, heights):
        n, res = len(heights), 0
        pse, nse, st = [-1] * n, [n] * n, []
        for i in range(n):
            while st and st[-1][0] >= heights[i]:
                st.pop()
            if st:
              pse[i] = st[-1][1]
            st.append((heights[i], i))
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and st[-1][0] >= heights[i]:
                st.pop()
            if st:
                nse[i] = st[-1][1]
            st.append((heights[i], i))
        for i in range(n):
            val = heights[i] * (nse[i] - pse[i] - 1)
            if val > res:
                res = val
        return res


print(Solution().largestRectangleArea(heights = [2,1,5,6,2,3]))
