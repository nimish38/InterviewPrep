# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.best = 0
        def getHeight(node):
            if not node:
                return 0
            left, right = getHeight(node.left), getHeight(node.right)
            self.best = max(self.best, left + right)
            return max(left, right) + 1
        getHeight(root)
        return self.best
    

a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right = b, c 
b.left, b.right = d, e
print(Solution().diameterOfBinaryTree(a))