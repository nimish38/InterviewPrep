class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p, q = head, head.next
        while q:
            r = q.next
            q.next = p
            p, q = q, r
        head.next = None
        return p

a, b, c, d, e, f = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)
a.next, b.next, c.next, d.next, e.next = b, c, d, e, f
x = Solution().reverseList(a)
print(x.val)