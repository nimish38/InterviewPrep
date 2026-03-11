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
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)