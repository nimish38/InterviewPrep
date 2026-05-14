class Solution(object):
    def countDigitOne(self, n):
        cnt = 0
        for _ in range(1, n + 1):
            cnt += str(_).count('1')
        return cnt

print(Solution().countDigitOne(13))