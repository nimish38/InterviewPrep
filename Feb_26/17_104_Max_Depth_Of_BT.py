class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        depth, st = 0, [root]
        while st:
            depth += 1
            for _ in range(len(st)):
                node = st.pop(0)
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
        return depth   
    

a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().maxDepth(a))