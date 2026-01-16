class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        n, self.pre = len(preorder), 0
        def constructBST(upper):
            if self.pre == n or preorder[self.pre] > upper:
                return None
            root = TreeNode(preorder[self.pre])
            self.pre += 1
            root.left = constructBST(root.val)
            root.right = constructBST(upper)
            return root
        return constructBST(float('inf'))


x = Solution().bstFromPreorder(preorder = [8,5,1,7,10,12])
print(x)