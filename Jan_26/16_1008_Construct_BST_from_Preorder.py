class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        inorder, n, self.pre = sorted(preorder), len(preorder), 0
        def constructBST(inLeft, inRight):
            if inRight < inLeft:
                return None
            root = TreeNode(preorder[self.pre])
            ind = inorder.index(root.val)
            self.pre += 1
            root.left = constructBST(inLeft, ind - 1)
            root.right = constructBST(ind + 1, inRight)
            return root
        return constructBST(0, n - 1)


x = Solution().bstFromPreorder(preorder = [8,5,1,7,10,12])
print(x)