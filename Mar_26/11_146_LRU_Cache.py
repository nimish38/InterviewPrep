class DoubleLL(object):
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache(object):
    def __init__(self, capacity):
        self.cap, self.map = capacity, {}
        self.head, self.tail = DoubleLL(0, -1), DoubleLL(-1, -1)
        self.head.next, self.head.prev = self.tail, None
        self.tail.next, self.tail.prev = None, self.head

    def get(self, key):
        if key not in self.map:
            return -1
        self.updateLRU(self.map[key], 'UPD')
        return self.map[key].val

    def put(self, key, value):
        if key not in self.map:
            if len(self.map) == self.cap:
                self.removeNode()
            node = DoubleLL(key, value)
            self.map[key] = node
            self.updateLRU(node, 'ADD')
        else:
            node = self.map[key]
            node.val = value
            self.updateLRU(node, 'UPD')

    def removeNode(self):
        last = self.tail.prev
        del self.map[last.key]
        new_last = last.prev
        new_last.next, self.tail.prev = self.tail, new_last

    def updateLRU(self, node, op):
        if op == 'UPD':        
            new_prev, new_next = node.prev, node.next
            new_prev.next, new_next.prev = new_next, new_prev
        first = self.head.next
        self.head.next, first.prev = node, node
        node.prev, node.next = self.head, first


lRUCache = LRUCache(2)
print(lRUCache.get(2))
lRUCache.put(2, 6)
print(lRUCache.get(1))
lRUCache.put(1, 5)
lRUCache.put(1, 2)
print(lRUCache.get(1))
print(lRUCache.get(2))