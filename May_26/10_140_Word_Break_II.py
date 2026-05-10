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


        for _ in range(len(res)):
            res[_] = ' '.join(res[_])
        return res

print(Solution().wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))