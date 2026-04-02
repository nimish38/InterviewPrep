class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        prev = None
        slow = fast = head
        # Reverse first half while finding middle
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next
        # Skip middle if odd length
        if fast:
            slow = slow.next
        # Compare
        while prev:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True

a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(2) ,ListNode(1),
print(Solution().isPalindrome(a))