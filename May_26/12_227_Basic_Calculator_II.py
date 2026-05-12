import operator


class Solution(object):
    def calculate(self, s):
        st, i, operations, num = [], 0, {'+': operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}, ''
        while i < len(s):
            if s[i] in operations:
                if num:
                    st.append(int(num))
                    num = ''
                if s[i] == '*' or s[i] == '/':
                    oper, op1, i = operations[s[i]], st.pop(), i + 1
                    while s[i] == ' ':
                        i += 1
                    while i < len(s) and s[i] not in operations and s[i] != ' ':
                        num += s[i]
                        i += 1
                    st.append(oper(op1, int(num)))
                    num, i = '', i - 1
                else:
                    st.append(s[i])
            elif s[i] == ' ':
                if num:
                    st.append(int(num))
                    num = ''
            else:
                num += s[i]
            i += 1

        res = st[0]
        for i in range(1, len(st), 2):
            oper, op2 = operations[st[i]], st[i + 1]
            res = oper(res, op2)
        return res

print(Solution().calculate(s = "3+2*2"))
