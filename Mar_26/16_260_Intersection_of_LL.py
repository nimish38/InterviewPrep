class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def reverse(head):
            p, q = head, head.next
            while q:
                r = q.next
                q.next = p
                p, q = q, r
            head.next = None
            return p 
        headA, headB, inter = reverse(headA), reverse(headB), None
        while headB == headA:
            inter = headA
            headA = headA.next
            headB = headB.next
        return inter