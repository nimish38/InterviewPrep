class Solution(object):
    def isAnagram(self, s, t):
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        for c in t:
            if c not in counter:
                return False
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
        return not counter

print(Solution().isAnagram(s = "anagram", t = "nagaram"))