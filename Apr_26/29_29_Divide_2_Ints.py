class Solution(object):
    def divide(self, dividend, divisor):
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign
        return sign * (dividend // divisor)