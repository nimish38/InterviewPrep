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
        self.best, mini, maxi = 0, float('-inf'), float('inf')
        def solve(node):
            if not node:
                return Custom(0, True, maxi, mini)
            left, right = solve(node.left), solve(node.right)
            if not left.isBST or not right.isBST or node.val <= left.maxRight or node.val >= right.maxLeft:
                return Custom(0, False, left.maxLeft,  right.maxRight)
            value = node.val + left.sum + right.sum
            self.best = max(self.best, value)
            return Custom(value, True, min(node.val, left.maxLeft), max(node.val, right.maxRight))
        solve(root)
        return self.best

a, b, c, d, e, f, g, h, i = TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(2), TreeNode(4), TreeNode(2), TreeNode(5), TreeNode(4), TreeNode(6)
# a.left, a.right, b.left, b.right, c.left, c.right, g.left, g.right = b, c, d, e, f, g, h , i
b.left, c.left, c.right = c, a, d
print(Solution().maxSumBST(b))