# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        cnt, curr, last = 0, head, None
        while curr:
            cnt += 1
            last = curr
            curr = curr.next
        cnt %= k
        if cnt == 0:
            return head
        else:
            first, second = head, head
            for _ in range(cnt):
                first = first.next
            while first.next:
                first = first.next
                second = second.next
            new_head = second.next
            second.next = None
            last.next = head
            return new_head
