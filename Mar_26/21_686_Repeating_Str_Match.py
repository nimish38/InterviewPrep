class Solution(object):
    def repeatedStringMatch(self, a, b):
        if len(set(b) - set(a)) > 0:
            return -1
        i, j, m, n = 0, 0, len(a), len(b)
        def checkRematch(x, y):
            cnt = 1
            while y < n and b[y] == a[x]:
                y += 1
                if x == m:
                    cnt += 1
                x = (x + 1) % m
            if y == n:
                return cnt
            return -1

        while i < m:
            while i < m and a[i] != b[j]:
                i += 1
            x = checkRematch(i, j)
            if x != -1:
                return x
            j = 0
        return -1