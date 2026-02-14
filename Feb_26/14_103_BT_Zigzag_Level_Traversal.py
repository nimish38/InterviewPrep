class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        st, res, kids, leftToRight = [root], [], [],  True

        def checkAndAdd(x):
            if x:
                kids.append(x)

        while st:
            n, lvl = len(st), []
            for _ in range(n):
                node = st.pop()
                lvl.append(node.val)
                if leftToRight:
                    checkAndAdd(node.left)
                    checkAndAdd(node.right)
                else:
                    checkAndAdd(node.right)
                    checkAndAdd(node.left)
            res.append(lvl)
            leftToRight = not leftToRight
            st, kids = kids, []
        return res


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right = b, c
b.left, c.right = d, e
print(Solution().zigzagLevelOrder(a))