class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k):
        seen = set()
        def dfs(node):
            if not node:
                return False 
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
    

a, b, c, d, e, f = TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(7)
a.left, a.right = b, c
b.left, b.right, c.right = d, e, f
print(Solution().findTarget(a, 9))