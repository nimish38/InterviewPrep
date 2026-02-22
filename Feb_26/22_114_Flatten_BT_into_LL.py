class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        curr, st = root, []
        while curr:
            if curr.right:
                st.append(curr.right)
            if curr.left:
                node, curr.left = curr.left, None
                curr.right = node
                curr = curr.right
            else:
                if st:
                    node, curr.left = st.pop(), None
                    curr.right = node
                    curr = curr.right
                else:
                    curr.left, curr.right = None, None
                    curr = curr.right
        return root


a, b, c, d, e, f =  TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
a.left, a.right = b, e
b.left, b.right, e.right = c, d, f
x = Solution().flatten(a)
print(x.val)