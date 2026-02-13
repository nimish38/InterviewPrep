from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        qu, res = deque([root]), []
        while qu:
            lvl, n = [], len(qu)
            for _ in range(n):
                node = qu.popleft()
                lvl.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            res.append(lvl)
        return res
