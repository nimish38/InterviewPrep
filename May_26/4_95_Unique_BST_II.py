import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        lower, upper = 1, n
        def genBST(l, r):
            if l > r:
                return [None]
            res = []
            for i in range(l, r + 1):
                node = TreeNode(i)
                X, Y = genBST(l, i - 1), genBST(i + 1, r)
                for dx in X:
                    node.left = dx
                    for dy in Y:
                        node.right = dy
                        res.append(copy.deepcopy(node))
            return res
        return genBST(lower, upper)

z = Solution().generateTrees(3)
print(z)