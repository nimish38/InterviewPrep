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

    def removeLFU(self):
        head, tail =  self.links[0]
        lfu_node = tail.prev
        tail.prev, lfu_node.prev.next = lfu_node.prev, tail
        head.val -= 1
        if head.val == 0:
            del self.links[0]
        del self.map[lfu_node.key]

    def addNode(self, cnt, node):
        if cnt not in self.links:
            head, tail = DLL('H', 1), DLL('T', -1)
            head.next, tail.prev = node, node
            node.next, node.prev = tail, head
            self.links[cnt] = [head, tail]
        else:
            head, tail = self.links[cnt]
            prev_mfu = head.next
            head.next, prev_mfu.prev = node, node
            node.next, node.prev = prev_mfu, head
            head.val += 1

    def removeNode(self, cnt, node):
        head, tail = self.links[cnt]
        if head.val == 1:
            del self.links[cnt]
        else:
            l, r = node.prev, node.next
            l.next, r.prev = r, l
            del node
            head.val -= 1


