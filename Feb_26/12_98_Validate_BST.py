class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

a, b, c, d, e = TreeNode(5), TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(6)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().isValidBST(a))