from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        indegree, adj, que, res = [0] * numCourses, defaultdict(list), deque(), 0
        for a,b in prerequisites:
            indegree[a] += 1
            adj[a].append(b)
        for _ in range(numCourses):
            if indegree[_] == 0:
                que.append(_)
                res += 1
        while que:
            course = que.popleft()
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)
                    res += 1
        return res == numCourses