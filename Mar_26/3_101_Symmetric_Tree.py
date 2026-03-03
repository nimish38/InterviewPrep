class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True

        return self.mirror(root.left,root.right)

    def mirror(self,right, left):
        if not right and not left:
            return True
        if not right or not left:
            return False
        if right.val != left.val:
            return False
        
        check_outside = self.mirror(left.left,right.right)
        check_inside = self.mirror(left.right,right.left)

        return check_outside and check_inside

        

        
                

