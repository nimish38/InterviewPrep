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
        memo = []
        for i in range(len(strs)):
            x = []
            for j in range(m + 1):
                x.append([-1] * (n + 1))
            memo.append(x)

        def solve(ind, zeros, ones):
            if ind >= len(strs):
                return 0
            if memo[ind][zeros][ones] == -1:
                take, skip= 0, 0
                z, o = getVals(strs[ind])
                if z <= zeros and o <= ones:
                    take = 1 + solve(ind + 1, zeros - z, ones - o)
                skip = solve(ind + 1, zeros, ones)
                memo[ind][zeros][ones] = max(take, skip)
            return memo[ind][zeros][ones]
        return solve(0, m, n)


print(Solution().findMaxForm(strs = ["10001110","11000","111110"], m = 5, n = 6))