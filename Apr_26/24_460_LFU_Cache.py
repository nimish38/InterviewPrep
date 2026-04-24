
class DLL(object):
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
        self.next = None
        self.prev = None

class LFUCache(object):
    def __init__(self, capacity):
        self.map, self.head, self.tail = {}, DLL(-1,-1,-1), DLL(-1,-1,-1)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
