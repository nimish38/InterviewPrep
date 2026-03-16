class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        lista = headA
        listb = headB
        while lista != listb:
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA 
        return listb
 
a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next, b.next, d.next, e.next = b, c, e, c
print(Solution().getIntersectionNode(a, d).val)