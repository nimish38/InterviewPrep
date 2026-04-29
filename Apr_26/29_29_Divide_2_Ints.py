class Solution(object):
    def divide(self, dividend, divisor):
        sign, upper, lower = 1, 2147483647, -2147483648
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign
        res = sign * (dividend // divisor)
        if res > upper:
            return upper
        if res < lower:
            return lower
        return res