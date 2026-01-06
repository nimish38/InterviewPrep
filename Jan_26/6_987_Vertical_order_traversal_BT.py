from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def verticalTraversal(self, root):
        st, cols, res = deque([(root, 0, 0)]), {}, []
        while st:
            for _ in range(len(st)):
                node, x, y = st.popleft()
                if y not in cols:
                    cols[y] = {}
                if x not in cols[y]:
                    cols[y][x] = []
                cols[y][x].append(node.val)

                if node.left:
                    st.append((node.left, x + 1, y - 1))
                if node.right:
                    st.append((node.right, x + 1, y + 1))

        for col in sorted(cols.keys()):
            temp = []
            for row in sorted(cols[col].keys()):
                for item in sorted(cols[col][row]):
                    temp.append(item)
            res.append(temp)
        return res


a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().verticalTraversal(a))