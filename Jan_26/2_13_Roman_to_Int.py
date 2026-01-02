class Solution:
    def romanToInt(self, s: str) -> int:
        vals, ans = {'I': (1, '-1'),'V': (5, 'I'),'X': (10, 'I'),'L':  (50, 'X'),'C': (100, 'X'),'D' : (500, 'C'),'M': (1000, 'C')}, 0
        for i in range(len(s)):
            if i == 0:
                ans += vals[s[i]][0]
            else:
                val, pre = vals[s[i]]
                ans += val
                if s[i - 1] == pre:
                    ans -= 2 * vals[pre][0]
        return ans

print(Solution().romanToInt(s = "MCMXCIV"))