class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        lower, upper = 1, n
        memo = [[-1] * n for _ in range(n)]
        def genBST(l, r):
            if l > r:
                return [None]
            if memo[l - 1][r - 1] == -1:
                res = []
                for i in range(l, r + 1):
                    X, Y = genBST(l, i - 1), genBST(i + 1, r)
                    for dx in X:
                        for dy in Y:
                            res.append(TreeNode(i, dx, dy))
                memo[l - 1][r - 1] = res
            return memo[l - 1][r - 1]
        return genBST(lower, upper)

z = Solution().generateTrees(3)
print(z)