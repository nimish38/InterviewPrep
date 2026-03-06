class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        return False

a ,b ,c, d = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
a.next, b.next, c.next, d.next = b, c, d, b
print(Solution().hasCycle(a))