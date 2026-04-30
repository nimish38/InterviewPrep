class Solution(object):
    def longestValidParentheses(self, s):
        st, best = [], 0
        for i in range(len(s)):
            if s[i] =='(':
                st.append(('(', i))
            else:
                if st and st[-1][0] == '(':
                    st.pop()
                    last = -1 if not st else st[-1][1]
                    best = max(best, i - last)
                else:
                    st.append((')', i))
        return best

print(Solution().longestValidParentheses(s = ")()())"))
