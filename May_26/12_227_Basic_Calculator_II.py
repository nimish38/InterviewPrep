class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        e = []
        n = 0
        f = '+'

        s = s.replace(" ", "") + '+'

        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            else:
                if f == '+':
                    e.append(n)
                elif f == '-':
                    e.append(-n)
                elif f == '*':
                    e.append(e.pop() * n)
                elif f == '/':
                    t = e.pop()
                    if t < 0:
                        e.append(- (abs(t) // n))  
                    else:
                        e.append(t // n)

                f = c
                n = 0

        return sum(e)