class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        st = [root]
        while st:
            level = []
            for _ in range(len(st)):
                node = st.pop(0)
                if node.left:
                    st.append(node.left)
                    level.append(node.left.val)
                else:
                    level.append('#')
                if node.right:
                    st.append(node.right)
                    level .append(node.right.val)
                else:
                    level.append('#')
            if level != level[::-1]:
                return False
        return True
                

