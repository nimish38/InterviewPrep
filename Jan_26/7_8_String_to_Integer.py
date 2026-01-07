class Solution(object):
    def myAtoi(self, s):
        sign, num, start = 1, '', False
        for char in s:
            if char == " " and not start:
                continue
            elif( char == '+' or char == '-' ) and not start:
                if char == '-':
                    sign =  -1
                start = True
            elif char.isdigit():
                num += char
                start = True
            else:
                break
        if num:
            num = int(num) * sign
            if num < -(2**31):
                return -(2**31)
            elif num > 2**31 - 1:
                return 2**31 - 1
            return num
        return 0

print(Solution().myAtoi(s = "0-1"))