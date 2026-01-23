# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        order, node, st = [], root, [root]
        while st:
            while node.left:
                node = node.left
                st.append(node)
            node = st.pop()
            order.append(node.val)
            if node.right:
                node = node.right
                st.append(node)
        return order



        
        
    

a, b, c, d, e = TreeNode(2), TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(5)
a.left, a.right = b, c
c.left, c.right = d, e
print(Solution().inorderTraversal(a)) 