class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root):
        self.st, self.curr = [], root
        while self.curr.left:
            self.st.append(self.curr)
            self.curr = self.curr.left

    def next(self) -> int:
        node = self.curr
        if node.right:
            self.curr = node.right
            while self.curr.left:
                self.st.append(self.curr)
                self.curr = self.curr.left
        else:
            if self.st:
                self.curr = self.st.pop()
            else:
                self.curr = None
        return node.val

    def hasNext(self) -> bool:
        if not self.curr and not self.st:
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
a, b, c, d, e = TreeNode(7), TreeNode(3), TreeNode(15), TreeNode(9), TreeNode(20)
a.left, a.right, c.left, c.right = b, c, d, e
obj = BSTIterator(a)
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())