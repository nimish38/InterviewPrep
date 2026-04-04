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
        node.next = None
