class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head):
        if not head: return None
        # insert new nodes in middle
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        # handle random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next
        # separate 2 lists
        curr, new_head = head.next, head.next
        while curr:
            if curr.next:
                curr.next = curr.next.next
            else:
                curr.next = None
            curr = curr.next
        return new_head