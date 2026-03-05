class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        mapping, curr = {}, head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            new = mapping[curr]
            new.next = mapping[curr.next]
            new.random = mapping[curr.random]
            curr = curr.next
        return mapping[head]
