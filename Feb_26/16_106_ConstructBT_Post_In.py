class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        self.post = len(postorder) - 1
        def build(inStart, inEnd):
            if inStart > inEnd:
                return None
            value = postorder[self.post]
            self.post -= 1
            node = TreeNode(value)
            ind = inorder.index(value)
            node.right = build(ind + 1, inEnd)
            node.left = build(inStart, ind - 1)
            return node
        return build(0, len(inorder) - 1)
    

x = Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print(x.val)