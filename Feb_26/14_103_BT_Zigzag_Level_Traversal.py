from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        st, res, leftToRight = deque([root]), [], True

        def checkAndAdd(x):
            if x:
                st.append(x)

        while st:
            n, lvl = len(st), []
            for _ in range(n):
                node = st.popleft()
                lvl.append(node.val)
                if leftToRight:
                    checkAndAdd(node.right)
                    checkAndAdd(node.left)
                else:
                    checkAndAdd(node.left)
                    checkAndAdd(node.right)
            res.append(lvl)
            leftToRight = not leftToRight
        return res


a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().zigzagLevelOrder(a))