class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def widthOfBinaryTree(self, root):
        st, isRoot, left, right, cnt, end, best = [root], True, True, True, -1, -1, -1
        while st and isRoot or ( left and right ):
            if not isRoot:
                left, right = False, False
            for _ in range(len(st)):
                node = st.pop(0)
                if node:
                    if not left:
                        left = True
                        cnt = 1
                    else:
                        cnt += 1
                        right = True
                        end = cnt
                    st.append(node.left)
                    st.append(node.right)
                else:
                    if left:
                        cnt += 1
                    st.extend([None, None])
            best = max(best, end)
            cnt, end, isRoot = -1, -1, False
        return best
    
a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(4), TreeNode(3), TreeNode(5), TreeNode(6)
a.left, a.right, b.left, b.right, c.right = b, c, d, e, f
print(Solution().widthOfBinaryTree(a))