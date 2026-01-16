class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        inorder, n = sorted(preorder), len(preorder)
        def constructBST(pre, ino):
            if not pre:
                return None
            root = TreeNode(pre[0])
            ind = ino.index(pre[0])
            root.left = constructBST(pre[1: ind + 1], ino[:ind])
            root.right = constructBST(pre[ind + 1:], ino[ind + 1:])
            return root

        return constructBST(preorder, inorder)