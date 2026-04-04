class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        succ, super = node.next, node.next.next
        while super:
            node.val = succ.val
            node, succ, super = succ, super, super.next
        node.val = succ.val
        node.next = None

a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next, b.next, c.next, d.next = b, c, d, e
Solution().deleteNode(b)
print(a)