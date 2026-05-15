class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        st, res = [(root, '')], []
        while st:
            node, path = st.pop()
            path += str(node.val) + '->'
            if not node.left and not node.right:
                res.append(path[: len(path) - 2])
                continue
            if node.left:
                st.append((node.left, path))
            if node.right:
                st.append((node.right, path))
        return res

a, b, c, d = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(5)
a.left = b
print(Solution().binaryTreePaths(a))