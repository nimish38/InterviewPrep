class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = curr = ListNode(-1)
        while list2 and list1:
            if list2.val <= list1.val:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
        if list2:
            curr.next = list2
        if list1:
            curr.next = list1
        return head.next

    def getLinkedList(self, arr):
        head = ListNode(-1)
        curr = head
        for elem in arr:
            curr.next = ListNode(elem)
            curr = curr.next
        return head.next


s = Solution()
a, b = s.getLinkedList([1,2,4]), s.getLinkedList([1,3,4])
x = s.mergeTwoLists(a, b)
print(x)

