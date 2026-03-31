class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None

a, b, c, d, e, f, g, h, i = TreeNode(6), TreeNode(2), TreeNode(8), TreeNode(0), TreeNode(4), TreeNode(7), TreeNode(9), TreeNode(3), TreeNode(5)
a.left, a.right, b.left, b.right, c.left, c.right, e.left, e.right = b, c, d, e, f, g, h, i
print(Solution().lowestCommonAncestor(a, h, i,).val)