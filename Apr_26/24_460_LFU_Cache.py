class DLL(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LFUCache(object):
    def __init__(self, capacity):
        self.map, self.links, self.cap = {}, {}, capacity

    def get(self, key):
        if key not in self.map:
            return -1
        cnt, node = self.map[key]
        self.removeNode(cnt, node)
        self.addNode(cnt + 1, node)
        self.map[key][1] += 1
        return node.val

    def put(self, key, value):
        if key not in self.map:
            if len(self.map) == self.cap:
                self.removeLFU()
            node = DLL(key, value)
            self.map[key] = [1, node]
            self.addNode(1, node)
        else:
            cnt, node = self.map[key]
            self.removeNode(cnt, node)
            self.addNode(cnt + 1, node)
            node.val = value

