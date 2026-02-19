class Solution(object):
    def maxNumOfSubstrings(self, s):
        chars, res = {}, []
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = [i, i]
            else:
                chars[s[i]][1] = i

        for key in chars:
            start, end = chars[key]
            st = [(start, end)]
            while st:
                curr_st, curr_ed = st.pop()
                for i in range(curr_st, curr_ed + 1):
                    new_st, new_ed = chars[s[i]]
                    if new_st < curr_st:
                        st.append((new_st, curr_st - 1))
                        start = new_st
                    if new_ed > curr_ed:
                        st.append((curr_ed + 1, new_ed))
                        end = new_ed
            chars[key] = [start, end]


print(Solution().maxNumOfSubstrings(s = "abbaccd"))