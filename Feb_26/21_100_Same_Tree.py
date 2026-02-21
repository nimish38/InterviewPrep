class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

a, b, c, x, y, z = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(1), TreeNode(2), TreeNode(3)
a.left, a.right, x.left, x.right =  c, b, y, z
print(Solution().isSameTree(a, x))