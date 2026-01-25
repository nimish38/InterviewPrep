class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def solve(ind, curr, combo):
            if curr == 0:
                res.append(list(combo))
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > curr:
                    break
                combo.append(candidates[i])
                solve(i + 1, curr - candidates[i], combo)
                combo.pop()

        solve(0, target, [])
        return res


print(Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))