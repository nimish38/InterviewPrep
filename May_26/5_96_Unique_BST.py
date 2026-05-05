class Solution(object):
    def numTrees(self, n):
        memo = [[-1] * n for _ in range(n)]
        def genBST(l, r):
            if l > r:
                return 1
            if memo[l - 1][r - 1] == -1:
                res = 0
                for i in range(l, r + 1):
                    X,Y = genBST(l, i - 1), genBST(i + 1, r)
                    res += X * Y
                memo[l - 1][r - 1] = res
            return memo[l - 1][r - 1]
        return genBST(1, n)

print(Solution().numTrees(5))