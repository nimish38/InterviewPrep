from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        res, que = str(root.val) + '#', deque([root])
        while que:
            node = que.popleft()
            if node.left:
                res += str(node.left.val) + '#'
                que.append(node.left)
            else:
                res += 'N#'
            if node.right:
                res += str(node.right.val) + '#'
                que.append(node.right)
            else:
                res += 'N#'
        return res

    def deserialize(self, data):
        if not data:
            return None
        data, ind, lvl = data.split('#'), 0, deque([])
        root = TreeNode(int(data[ind]))
        ind += 1
        lvl.append(root)
        while lvl:
            node, l, r = lvl.popleft(), data[ind], data[ind + 1]
            if l != 'N':
                node.left = TreeNode(int(l))
                lvl.append(node.left)
            if r != 'N':
                node.right = TreeNode(int(r))
                lvl.append(node.right)
            ind += 2
        return root

a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right, c.left, c.right = b, c, d, e
x = Codec().serialize(a)
y = Codec().deserialize(x)
print(y)