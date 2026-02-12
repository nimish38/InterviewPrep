class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        def isValid(node, left, right):
            if not node:
                return True
            if not left < node.val < right:
                return False
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        return isValid(root, float('-inf'), float('inf'))


a, b, c, d, e = TreeNode(5), TreeNode(1), TreeNode(8), TreeNode(6), TreeNode(10)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().isValidBST(a))