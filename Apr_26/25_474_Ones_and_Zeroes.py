class Solution(object):
    def findMaxForm(self, strs, m, n):

        def getVals(s):
            z,o = 0, 0
            for c in s:
                if c == '0':
                    z += 1
                else:
                    o += 1
            return z, o

        strs.sort(key=lambda x:len(x))
        res, i = 0, 0
        while m > 0 or n > 0:
            zer, one = getVals(strs[i])
            if zer <= m and one <= n:
                m -= zer
                n -= one
                res += 1
            i += 1
        return res


print(Solution().findMaxForm(strs = ["10","0","1"], m = 1, n = 1))