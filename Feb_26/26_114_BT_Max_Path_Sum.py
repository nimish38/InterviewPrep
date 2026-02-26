class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        self.best = float('-inf')
        def get_max_path(node):
            if not node:
                return 0
            left, right = get_max_path(node.left), get_max_path(node.right)
            value = left + right + node.val
            self.best = max(self.best, node.val, value, node.val + left, node.val + right)
            return max(node.val, node.val + max(left, right))
        get_max_path(root)
        return self.best
    

a, b, c, d, e, p, q, r, s = TreeNode(9), TreeNode(6), TreeNode(-3), TreeNode(-6), TreeNode(2), TreeNode(2),TreeNode(-6),TreeNode(-6),TreeNode(-6)
a.left, a.right = b, c
c.left, c.right = d, e
e.left, p.left, p.right, q.left = p, q, r, s
print(Solution().maxPathSum(a))