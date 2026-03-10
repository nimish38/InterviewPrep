class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        if not root: return []
        res, st = [], [root]
        while st:
            node = st.pop()
            res.append(node.val)
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return res[::-1]