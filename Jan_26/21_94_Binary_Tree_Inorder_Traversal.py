# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.order = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.order.append(node.val)
            inorder(node.right)
        inorder(root)
        return self.order
    

a, b, c, d, e = TreeNode(2), TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(5)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().inorderTraversal(a)) 