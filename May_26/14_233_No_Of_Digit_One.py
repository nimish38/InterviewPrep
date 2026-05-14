class Solution(object):
    def countDigitOne(self, n):
        n = str(n)
        def solve(ind, tight, cnt):
            if ind == len(n):
                return cnt
            lower, res = 0, 0
            if tight:
                upper = int(n[ind])
            else:
                upper = 9
            for dig in range(lower, upper + 1):
                isTight, isOne = dig == upper, 1 if dig == 1 else 0
                res += solve(ind + 1, tight and isTight, cnt + isOne)
            return res

        return solve(0, True, 0)

print(Solution().countDigitOne(13))