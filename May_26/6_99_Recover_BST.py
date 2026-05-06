class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        st, prev, first, last, curr = [], TreeNode(float('-inf')), None, None, root
        while curr:
            st.append(curr)
            curr = curr.left
        while st:
            curr = st.pop()
            if curr.val < prev.val:
                if not first:
                    first, last = prev, curr
                else:
                    last = curr
            prev = curr
            if curr.right:
                curr = curr.right
                while curr:
                    st.append(curr)
                    curr = curr.left
        first.val, last.val = last.val, first.val
        return root


a, b, c, d = TreeNode(3), TreeNode(1), TreeNode(4), TreeNode(2)
a.left, a.right, c.left = b, c, d
z = Solution().recoverTree(a)
print(z)
