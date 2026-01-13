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