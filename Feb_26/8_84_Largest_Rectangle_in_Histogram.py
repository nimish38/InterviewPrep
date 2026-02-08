class Solution(object):
    def largestRectangleArea(self, heights):
        n, res, st = len(heights), 0, []
        for i in range(n):
            while st and st[-1][0] > heights[i]:
                val, nse, pse = st.pop()[0], i, -1
                if st:
                    pse = st[-1][1]
                area = val * (nse - pse -1)
                if area > res:
                    res = area
            st.append((heights[i], i))
        nse = n
        while st:
            val, pse = st.pop()[0], -1
            if st:
                pse = st[-1][1]
            area = val * (nse - pse - 1)
            if area > res:
                res = area
        return res


print(Solution().largestRectangleArea(heights = [2,1,5,6,2,3]))
