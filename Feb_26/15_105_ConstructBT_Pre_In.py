class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        self.pre = 0
        def build(inStart, inEnd):
            if inStart > inEnd:
                return None
            val = preorder[self.pre]
            self.pre += 1
            ind = inorder.index(val)
            node = TreeNode(val)
            node.left = build(inStart, ind - 1)
            node.right = build(ind + 1, inEnd)
            return node
        return build(0, len(inorder) - 1)


x = Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
print(x)