# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxSumBST(self, root):
        self.best= 0
        def solve(node):
            if not node:
                return 0, True
            left, right = solve(node.left),solve(node.right)
            isBST = left[1] and right[1]
            if not isBST:
                return 0, False
            if node.left and node.left.val >= node.val or node.right and node.right.val <= node.val:
                isBST = False
            if isBST:
                value = left[0] + right[0] + node.val
                self.best = max(self.best, value)
                return value, True
            return 0, False
        solve(root)
        return self.best

a, b, c, d, e, f, g, h, i = TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(2), TreeNode(4), TreeNode(2), TreeNode(5), TreeNode(4), TreeNode(6)
a.left, a.right, b.left, b.right, c.left, c.right, g.left, g.right = b, c, d, e, f, g, h , i
print(Solution().maxSumBST(a))