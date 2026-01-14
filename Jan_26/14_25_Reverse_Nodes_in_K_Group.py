class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        dummy = prev_tail = ListNode(-1)
        curr, prev_tail.next = head, head
        while True:
            for _ in range(k):
                if not curr:
                    return dummy.next
                curr = curr.next
            new_head, new_tail = self.reverseLL(prev_tail.next, k)
            prev_tail.next = new_head
            new_tail.next = curr
            prev_tail = new_tail

    def reverseLL(self, node, k):
        first, second = node, node.next
        tail = first
        for _ in range(k - 1):
            temp = second.next
            second.next = first
            first, second = second, temp
        return first, tail

    def getLinkedList(self, arr):
        head = ListNode(-1)
        curr = head
        for elem in arr:
            curr.next = ListNode(elem)
            curr = curr.next
        return head.next


s = Solution()
a = s.getLinkedList([1,2,3,4,5])
x = s.reverseKGroup(a, 3)
print(x)