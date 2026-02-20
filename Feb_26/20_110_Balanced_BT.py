class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        def solve(node):
            if not node:
                return 1
            left, right = solve(node.left), solve(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return solve(root) != -1


a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().isBalanced(a))