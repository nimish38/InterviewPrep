class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        self.best = 0
        def get_max_path(node):
            if not node:
                return 0
            left, right = get_max_path(node.left), get_max_path(node.right)
            value = left + right + node.val
            if value > self.best:
                self.best = value
            return node.val + max(left, right)
        get_max_path(root)
        return self.best
    

a, b, c, d, e = TreeNode(-10), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7), 
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().maxPathSum(a))