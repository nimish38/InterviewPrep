class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def widthOfBinaryTree(self, root):
        st, isRoot, left, right, cnt, end, best = [root], True, False, False, -1, -1, -1
        while st and isRoot or ( left != -1 and right != -1 ):
            left, right = False, False
            for _ in range(len(st)):
                node = st.pop()
                if node:
                    if not left:
                        left = True
                        cnt = 1
                    else:
                        cnt += 1
                        if not right:
                            right = True
                            end = cnt
                    st.append(node.left)
                    st.append(node.right)
                else:
                    st.extend([None, None])
            best = max(best, end)
            cnt, end= -1, -1
        return best