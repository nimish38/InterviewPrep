class DoubleLL(object):
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache(object):
    def __init__(self, capacity):
        self.cap, self.map = capacity, {}
        self.head, self.tail = DoubleLL(-1), DoubleLL(-1)
        self.head.next, self.head.prev = self.tail, None
        self.tail.next, self.tail.prev = None, self.head

    def get(self, key):
        if key not in self.map:
            return -1
        self.updateLRU(self.map[key])
        return self.map[key].val

    def put(self, key, value):
        if len(self.map) == self.cap:
            self.removeNode()
        node = DoubleLL(value)
        self.map[key] = node
        self.updateLRU(node)

    def removeNode(self):
        last = self.tail.prev
        new_last = last.prev
        new_last.next, self.tail.prev = self.tail, new_last

    def updateLRU(self, node):
        new_prev, new_next = node.prev, node.next
        new_prev.next, new_next.prev = new_next, new_prev
        first = self.head.next
        self.head.next, first.prev = node, node
        node.prev, node.next = self.head, first


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)