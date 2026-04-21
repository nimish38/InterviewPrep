# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        self.ans = 0

        def dfs(node):
            if not node:  #
                return True, None, None, 0

            l_bst, l_min, l_max, l_sum = dfs(node.left)
            r_bst, r_min, r_max, r_sum = dfs(node.right)

            if (l_bst and r_bst and
                    (l_max is None or l_max < node.val) and
                    (r_min is None or node.val < r_min)):
                total = l_sum + r_sum + node.val
                self.ans = max(self.ans, total)

                new_min = l_min if l_min is not None else node.val
                new_max = r_max if r_max is not None else node.val

                return True, new_min, new_max, total

            return False, None, None, 0

        dfs(root)
        return self.ans


a, b, c, d, e, f, g, h, i = TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(2), TreeNode(4), TreeNode(2), TreeNode(5), TreeNode(4), TreeNode(6)
# a.left, a.right, b.left, b.right, c.left, c.right, g.left, g.right = b, c, d, e, f, g, h , i
b.left, c.left, c.right = c, a, d
print(Solution().maxSumBST(b))