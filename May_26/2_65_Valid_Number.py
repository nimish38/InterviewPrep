class Solution(object):
    def isNumber(self, s):
        sign1, sign2, expo, deci, nums, left, right = False, False, False, False, {'0', '1','2', '3', '4', '5', '6', '7', '8', '9'}, False, False
        for i in range(len(s)):
            c = s[i]
            if c == '+' or c =='-':
                if i == 0 or s[i - 1] == 'e' or s[i - 1] == 'E':
                    if not sign1:
                        sign1 = True
                    elif expo and not sign2:
                        sign2 = True
                    else:
                        return False
                else:
                    return False
            elif c == '.':
                if not deci and not expo:
                    deci = True
                else:
                    return False
            elif c == 'e' or c == 'E':
                if left and not expo:
                    expo = True
                else:
                    return False
            elif c in nums:
                if not expo and not left:
                    left = True
                if expo and not right:
                    right = True
            else:
                return False
        return left if not expo else left and right


print(Solution().isNumber("-1E+3"))
