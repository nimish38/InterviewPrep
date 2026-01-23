class Solution(object):
    def combinationSum(self, candidates, target):
        n, res = len(candidates), []
        def solve(ind, curr, combo):
            if curr == target:
                res.append(combo.copy())
                return
            if ind >= n:
                return
            for i in range(ind, n):
                if curr + candidates[i] <= target:
                    combo.append(candidates[i])
                    solve(i, curr + candidates[i], combo)
                    combo.pop()

        solve(0, 0, [])
        return res
        

print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))