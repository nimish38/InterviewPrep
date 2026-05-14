class Solution(object):
    def countDigitOne(self, n):
        n, memo = str(n), []
        for i in range(11):
            x = []
            for j in range(10):
                x.append([-1] * 2)
            memo.append(x)
        # print(memo)

        def solve(ind, tight, cnt):
            if ind == len(n):
                return cnt
            # print(ind, tight, cnt)
            if memo[ind][cnt][tight] == -1:
                lower, res = 0, 0
                if tight:
                    upper = int(n[ind])
                else:
                    upper = 9
                for dig in range(lower, upper + 1):
                    isTight, isOne = 1 if dig == upper and tight else 0, 1 if dig == 1 else 0
                    res += solve(ind + 1, isTight, cnt + isOne)
                memo[ind][cnt][tight] = res
            return memo[ind][cnt][tight]

        return solve(0, 1, 0)

print(Solution().countDigitOne(1000))