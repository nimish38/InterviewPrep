class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def findLength(head):
            p, cnt = head, 0
            while p:
                cnt += 1
                p = p.next
            return cnt
        def moveAhead(head, val):
            for _ in range(val):
                head = head.next
            return head
        l1, l2 = findLength(headA), findLength(headB)
        diff = l1 - l2
        if diff > 0:
            headA = moveAhead(headA, diff)
        else:
            headB = moveAhead(headB, abs(diff))
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


    
a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next, b.next, d.next, e.next = b, c, e, c
print(Solution().getIntersectionNode(a, d).val)