import operator


class Solution(object):
    def calculate(self, s):
        st, i, operations = [], 0, {'+': operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                st.append(s[i])
            elif s[i] == '*' or s[i] == '/':
                op1, op2 = st.pop(), int(s[i + 1])
                st.append(operations[s[i]](op1, op2))
                i += 1
            elif s[i] == ' ':
                continue
            else:
                st.append(int(s[i]))
