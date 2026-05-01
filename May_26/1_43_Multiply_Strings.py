class Solution(object):
    def multiply(self, num1, num2):
        res = 0
        for i in range(len(num2) - 1, -1, -1):
            digit, carry, val, curr = int(num2[i]), 0, '', 0
            for j in range(len(num1) - 1, -1, -1):
                curr = (digit * int(num1[j])) + carry
                if curr > 9:
                    carry = curr // 10
                    curr %= 10
                else:
                    carry = 0
                val = str(curr) + val
            if carry:
                val = str(carry) + val
            val += '0' * (len(num2) - i - 1)
            res += int(val)
        return str(res)

print(Solution().multiply(num1 = "123", num2 = "456"))