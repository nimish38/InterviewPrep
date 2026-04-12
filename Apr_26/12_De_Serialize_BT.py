from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
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
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))