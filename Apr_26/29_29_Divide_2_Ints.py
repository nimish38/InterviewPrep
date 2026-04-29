class Solution(object):
    def divide(self, dividend, divisor):
        sign, res, upper, lower = True, 0, 2147483647, -2147483648
        if (dividend < 0 < divisor) or (dividend > 0 > divisor):
            sign = False
        divisor, dividend = abs(divisor), abs(dividend)
        while dividend >= divisor:
            i = 0
            while divisor << (i + 1) <= dividend:
                i += 1
            res += 1 << i
            dividend -= divisor << i
        if not sign:
            res = -res
        if res > upper:
            return upper
        if res < lower:
            return lower
        return res