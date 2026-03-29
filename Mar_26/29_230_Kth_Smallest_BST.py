class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        inorder, st, curr = [], [], root
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop(0)
            inorder.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = None
            if len(inorder) == k - 1:
                return inorder[-1]
        return inorder[-1]





