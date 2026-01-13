class Solution(object):
    def isValid(self, s):
        st, match = [], {'}':'{', ']':'[', ')': '('}
        for c in s:
            if c in match:
                if not st or st[-1] != match[c]:
                    return False
                else:
                    st.pop()
            else:
                st.append(c)
        return len(st) == 0


print(Solution().isValid(s = "([])"))