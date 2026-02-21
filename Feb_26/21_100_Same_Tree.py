class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        s1, s2 = [p], [q]
        while s1 and s2:
            n1, n2 = s1.pop(), s2.pop()
            if n1.val != n2.val:
                return False
            if n1.left and n2.left:
                s1.append(n1.left)
                s2.append(n2.left)
            elif n1.left or n2.left:
                return False
            if n1.right and n2.right:
                s1.append(n1.right)
                s2.append(n2.right)
            elif n1.right or n2.right:
                return False
        if s1 or s2:
            return False
        return True

a, b, c, x, y, z = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(1), TreeNode(2), TreeNode(3)
a.left, a.right, x.left, x.right =  b, c, y, z
print(Solution().isSameTree(a, x))