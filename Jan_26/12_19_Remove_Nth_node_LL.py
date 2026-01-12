class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next, first, second = head, dummy, dummy
        for _ in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
# a.next, b.next, c.next, d.next = b, c, d, e
x = Solution().removeNthFromEnd(a, 1)
print(x.val)

