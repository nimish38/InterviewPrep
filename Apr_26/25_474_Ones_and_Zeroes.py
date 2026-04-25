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

        def solve(ind, zeros, ones):
            if ind >= len(strs):
                return 0
            take, skip= 0, 0
            z, o = getVals(strs[ind])
            if z <= zeros and o <= ones:
                take = 1 + solve(ind + 1, zeros - z, ones - o)
            skip = solve(ind + 1, zeros, ones)
            return max(take, skip)

        return solve(0, m, n)


print(Solution().findMaxForm(strs = ["10001110","11000","111110"], m = 6, n = 6))