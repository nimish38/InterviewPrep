class Solution(object):
    def divide(self, dividend, divisor):
        sign, res, upper, lower = 1, 0, 2147483647, -2147483648
        if (dividend < 0 < divisor) or (dividend > 0 > divisor):
            sign = -1
        divisor, dividend = abs(divisor), abs(dividend)
        while dividend >= divisor:
            i = 0
            while divisor * (2 ** i) <= dividend:
                i += 1
            i -= 1
            res += 2 ** i
            dividend -= divisor * (2 ** i)
        res = sign * res
        if res > upper:
            return upper
        if res < lower:
            return lower
        return res