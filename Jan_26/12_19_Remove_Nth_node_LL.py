class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy,  = ListNode(-1)
        dummy.next, first, second = head, dummy, dummy
        for _ in range(n):
            first = first.next
        while second.next:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next




