class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        st, res = [(root, str(root.val))], []
        while st:
            node, path = st.pop()
            path += '->' + str(node.val)
            if not node.left and not node.right:
                res.append(path)
                continue
            if node.left:
                st.append((node.left, path))
            st.append((node.right, path))
        return res

