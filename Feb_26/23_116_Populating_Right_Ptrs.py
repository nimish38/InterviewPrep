class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root


a, b, c, d, e, f, g = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
a.left, a.right = b, c
b.left, b.right, c.left, c.right = d, e, f, g
x = Solution().connect(a)
print(x)
