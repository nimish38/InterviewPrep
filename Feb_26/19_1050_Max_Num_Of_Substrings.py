class Solution(object):
    def maxNumOfSubstrings(self, s):
        chars, res = {}, []
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = 1
            else:
                if chars[s[i]] == -1:
                    continue
                elif s[i - 1] == s[i]:
                    chars[s[i]] += 1
                else:
                    chars[s[i]] = -1

        for key in chars:
            if chars[key] != -1:
                res.append(key * chars[key])
        return res


print(Solution().maxNumOfSubstrings(s = "adefaddaccc"))