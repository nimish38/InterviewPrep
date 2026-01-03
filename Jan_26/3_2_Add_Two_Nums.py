class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry, res = 0, ListNode(-1)
        l3 = res
        while l1 and l2:
            value = l1.val + l2.val + carry
            l3.next = ListNode(value % 10)
            carry = value // 10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        while l1:
            value = l1.val + carry
            l3.next = ListNode(value % 10)
            carry = value // 10
            l1 = l1.next
            l3 = l3.next
        while l2:
            value = l2.val + carry
            l3.next = ListNode(value % 10)
            carry = value // 10
            l2 = l2.next
            l3 = l3.next

        if carry:
            l3.next = ListNode(1)
        return res.next

    def getLinkedList(self, arr):
        head = ListNode(-1)
        curr = head
        for elem in arr:
            curr.next = ListNode(elem)
            curr = curr.next
        return head

    def printLinkedList(self, L):
        while L:
            print(L.val, end='-> ')
            L = L.next
        print('None')

S = Solution()
l1, l2 = [9,9,9,9,9,9,9],[9,9,9,9]
l3 = S.addTwoNumbers(S.getLinkedList(l1).next, S.getLinkedList(l2).next)
S.printLinkedList(l3)