class Solution(object):
    def numTrees(self, n):
        def genBST(l, r):
            if l > r:
                return 1
            res = 0
            for i in range(l, r + 1):
                X,Y = genBST(l, i - 1), genBST(i + 1, r)
                for dx in range(X):
                    for dy in range(Y):
                        res += 1
            return res
        return genBST(1, n)

print(Solution().numTrees(4))