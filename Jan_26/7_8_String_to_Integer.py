class Solution(object):
    def myAtoi(self, s):
        sign, num, start = 1, 0, False
        for char in s:
            if char == " " and not start:
                continue
            elif char == '+' or char == '-' and not start:
                if char == '-':
                    sign =  -1
                start = True

            elif 47 < ord(char) < 58:
                num *= 10
                num += int(char)
                start = True
            else:
                break

        num *= sign
        if num < -(2**31):
            return -(2**31)
        elif num > 2**31:
            return 2**31
        return num

print(Solution().myAtoi(s = "-137z42"))