class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTarget(self, root, k):
        seen, st = {}, [root]
        while st:
            node = st.pop(0)
            if k - node.val in seen:
                return True
            seen[node.val] = 1
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return False
    

a, b, c, d, e, f = TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(7)
a.left, a.right = b, c
b.left, b.right, c.right = d, e, f
print(Solution().findTarget(a, 9))