class Solution(object):
    def longestValidParentheses(self, s):
        st, best = [-1], 0
        for i in range(len(s)):
            if s[i] =='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    best = max(best, i - st[-1])
        return best

print(Solution().longestValidParentheses(s = ")()())"))
