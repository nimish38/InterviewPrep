class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        if not root:
            return None
        st, kids = [root], []
        while st:
            for _ in range(len(st)):
                node = st.pop(0)
                if not st:
                    node.next = None
                else:
                    node.next = st[0]
                if node.left:
                    kids.append(node.left)
                if node.right:
                    kids.append(node.right)
            st, kids = kids, []
        return root


a, b, c, d, e, f, g = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
a.left, a.right = b, c
b.left, b.right, c.left, c.right = d, e, f, g
x = Solution().connect(a)
print(x)
