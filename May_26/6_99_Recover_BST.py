class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        nodes, curr, inorder, st = {}, root, [], []
        while curr:
            st.append(curr)
            curr = curr.left
        while st:
            curr = st.pop()
            inorder.append(curr.val)
            nodes[curr.val] = curr
            if curr.right:
                curr = curr.right
                while curr:
                    st.append(curr)
                    curr = curr.left
        correct_inorder = sorted(inorder.copy())
        for _ in range(len(inorder)):
            if inorder[_] != correct_inorder[_]:
                nodes[inorder[_]].val, nodes[correct_inorder[_]].val = correct_inorder[_], inorder[_]
                break
        return root


a, b, c, d = TreeNode(3), TreeNode(1), TreeNode(4), TreeNode(2)
a.left, a.right, c.left = b, c, d
z = Solution().recoverTree(a)
print(z)
