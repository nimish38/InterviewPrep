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
            p, p = q, r
        return p

