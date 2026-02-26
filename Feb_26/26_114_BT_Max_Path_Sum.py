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
            val = left + right + node.val
            if val > self.best:
                self.best = val
            return val + max(left, right)
        get_max_path(root)
        return self.best
    
