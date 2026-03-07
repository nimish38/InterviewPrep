class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        nodes, curr = set(), head
        while curr:
            if curr in nodes:
                return curr
            nodes.add(curr)
            curr = curr.next
        return False
