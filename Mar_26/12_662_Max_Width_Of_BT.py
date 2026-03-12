from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        st, best, width = deque([(root, 0)]), 1, -1
        while st:
            for _ in range(len(st)):
                node, ind = st.popleft()
                if node.left:
                    st.append((node.left, ind * 2))
                if node.right:
                    st.append((node.right, 1 + (ind * 2)))
            if len(st) >= 2:
                width = 1 - st[0][1] + st[-1][1]
            best = max(width, best)
        return best              
    
a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(4), TreeNode(3), TreeNode(5), TreeNode(6)
a.left, a.right, b.left, b.right, c.right = b, c, d, e, f
print(Solution().widthOfBinaryTree(a))