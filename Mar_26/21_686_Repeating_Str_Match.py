class Solution:
    def repeatedStringMatch(self, a, b):
        if set(b) - set(a):
            return -1
        n, m = len(a), len(b)
        k = (m + n - 1) // n
        s = a * k
        if b in s:
            return k
        if b in s + a:
            return k + 1
        return -1