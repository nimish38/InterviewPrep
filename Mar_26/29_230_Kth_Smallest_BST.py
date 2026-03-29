class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        st, curr = [], root
        while curr:
            st.append(curr)
            curr = curr.left
        while st:
            curr = st.pop()
            k -= 1
            if k == 0:
                return curr.val
            if curr.right:
                curr = curr.right
                while curr:
                    st.append(curr)
                    curr = curr.left
        return curr.val


a, b, c, d, e, f = TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(1)
a.left, a.right, b.left, b.right, d.left = b, c, d, e, f
print(Solution().kthSmallest(a, 6))

