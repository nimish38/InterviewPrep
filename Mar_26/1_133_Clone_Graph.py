class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        mapping = {}
        def dfs(root):
            if root not in mapping:
                mapping[root] = Node(root.val)
            for nei in root.neighbors:
                if nei not in mapping:
                    dfs(nei)
        for node in mapping:
            for nei in node.neighbors:
                mapping[node].neighbors.append(mapping[nei])
        dfs(node)
        return mapping[node]