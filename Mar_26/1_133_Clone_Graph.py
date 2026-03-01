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
        dfs(node)
        for nodes in mapping:
            for nei in nodes.neighbors:
                mapping[nodes].neighbors.append(mapping[nei])
        return mapping[node]

    def buildGraph(self, nodes, adj):
        for i in range(1, len(nodes)):
            for neig in adj[i - 1]:
                nodes[i].neighbors.append(nodes[neig])
        return nodes[1]

a, b, c, d = Node(1), Node(2), Node(3), Node(4)
y =Solution().buildGraph([1, a, b, c, d], [[2,4],[1,3],[2,4],[1,3]])
x = Solution().cloneGraph(y)
print(x.val)
