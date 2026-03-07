class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow, fast, cycle = head, head, False
        while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
           if slow == fast:
               cycle = True
               break
        if not cycle:
            return None
        entry = head
        while entry != slow:
            entry = entry.next
            slow = slow.next
        return entry

a ,b ,c, d = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
a.next, b.next, c.next, d.next = b, c, d, b
print(Solution().detectCycle(a).val)