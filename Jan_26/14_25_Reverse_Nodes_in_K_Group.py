class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        if k == 1:
            return head

    def reverseLL(self, node, k):
        first, second = node, node.next
        tail = first
        for _ in range(k - 1):
            temp = second.next
            second.next = first
            first, second = second, temp
        return first, tail