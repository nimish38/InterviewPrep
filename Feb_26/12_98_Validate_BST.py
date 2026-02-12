class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        st = [[root, float('-inf'), float('inf')]]
        while st:
            node, left, right = st.pop(0)
            if not left < node.val < right:
                return False
            if node.left:
                st.append([node.left, left, node.val])
            if node.right:
                st.append(([node.right, node.val, right]))
        return True

a, b, c, d, e = TreeNode(5), TreeNode(1), TreeNode(8), TreeNode(6), TreeNode(10)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().isValidBST(a))