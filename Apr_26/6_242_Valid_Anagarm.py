class Solution(object):
    def isAnagram(self, s, t):
        s, t = sorted(list(s)), sorted(list(t))
        return s == t

print(Solution().isAnagram(s = "anasgram", t = "nagaram"))