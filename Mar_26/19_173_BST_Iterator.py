class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root):
        self.inorder, self.curr = [-1], 0
        self.traverse(root)

    def traverse(self, node):
        if node.left:
            self.traverse(node.left)
        self.inorder.append(node.val)
        if node.right:
            self.traverse(node.right)

    def next(self) -> int:
        self.curr += 1
        return self.inorder[self.curr]

    def hasNext(self) -> bool:
        if self.curr == len(self.inorder) - 1:
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