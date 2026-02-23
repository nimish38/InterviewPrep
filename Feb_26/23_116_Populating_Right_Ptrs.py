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