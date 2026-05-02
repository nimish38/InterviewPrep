class Solution(object):
    def isNumber(self, s):
        sign1, sign2, expo, deci, nums, left, right = False, False, False, False, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, False, False
        for c in s:
            if c == '+' or c =='-':
                if not sign1:
                    sign1 = True
                elif expo and not sign2:
                    sign2 = True
                else:
                    return False
            if c == '.':
                if not deci and not expo:
                    deci = True
                else:
                    return False
            if c == 'e' or c == 'E':
                if not expo:
                    expo = True
                else:
                    return False
            if c in nums:
                if not expo and not left:
                    left = True
                if expo and not right:
                    right = True
            else:
                return False
        return left and right
