class Solution(object):
    def longestValidParentheses(self, s):
        st, best = [], 0
        for i in range(len(s)):
            if s[i] =='(':
                st.append(i)
            elif s[i] == ')' and st:
                st.pop()
                last = 0 if not st else st[-1]
                best = max(best, i - last)
        return best

print(Solution().longestValidParentheses(s = ")()())"))
