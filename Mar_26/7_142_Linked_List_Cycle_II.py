class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow, fast, cycle = head, head, False
        while fast.next:
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
