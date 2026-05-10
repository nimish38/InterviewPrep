class Solution(object):
    def wordBreak(self, s, wordDict):
        n, res, wordDict = len(s), [], set(wordDict)
        def solve(ind, curr):
            if ind >= n:
                res.append(curr.copy())
                return
            for i in range(1, n - ind + 1):
                if s[ind: ind + i] in wordDict:
                    curr.append(s[ind: ind + i])
                    solve(ind + i, curr)
                    curr.pop()
        solve(0, [])
        return res

print(Solution().wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))