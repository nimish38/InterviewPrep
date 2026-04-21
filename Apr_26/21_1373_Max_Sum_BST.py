# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Custom(object):
    def __init__(self, sum, isBST, maxLeft, maxRight):
        self.sum = sum
        self.isBST = isBST
        self.maxLeft = maxLeft
        self.maxRight = maxRight

class Solution(object):
    def maxSumBST(self, root):
        self.best = 0
        def solve(node):
            if not node:
                return Custom(0, True, None, None)
            left, right = solve(node.left), solve(node.right)
            if left.isBST and right.isBST and (left.maxRight is None or left.maxRight < node.val) and (right.maxLeft is None or node.val < right.maxLeft):
                value = node.val + left.sum + right.sum
                self.best = max(self.best, value)
                new_min = left.maxLeft if left.maxLeft is not None else node.val
                new_max = right.maxRight if right.maxRight is not None else node.val
                return Custom(value, True, new_min, new_max)
            return Custom(0, False, None, None)

        solve(root)
        return self.best

a, b, c, d, e, f, g, h, i = TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(2), TreeNode(4), TreeNode(2), TreeNode(5), TreeNode(4), TreeNode(6)
# a.left, a.right, b.left, b.right, c.left, c.right, g.left, g.right = b, c, d, e, f, g, h , i
b.left, c.left, c.right = c, a, d
print(Solution().maxSumBST(b))