class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        vals = '#'
        while head:
            vals += str(head.val) + '#'
            head = head.next
        return vals == vals[::-1]

a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(2) ,ListNode(1),
print(Solution().isPalindrome(a))