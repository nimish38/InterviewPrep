class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def solve(node):
            if not node or node == p or node == q:
                return node
            left, right = solve(node.left), solve(node.right)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None
        return solve(root)

