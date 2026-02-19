class Solution(object):
    def maxNumOfSubstrings(self, s):
        chars, res, seen = {}, [], []
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
                    if new_st < start:
                        st.append((new_st, start - 1))
                        start = new_st
                    if new_ed > end:
                        st.append((end + 1, new_ed))
                        end = new_ed
            chars[key] = [start, end]

        sorted_substrings = sorted(chars.values(), key= lambda x:x[1] - x[0])
        for start, end in sorted_substrings:
            if any( sta <= end and start <= ed for sta, ed in seen):
                continue
            res.append(s[start: end + 1])
            seen.append((start, end))
        return res


print(Solution().maxNumOfSubstrings(s = "adefaddaccc"))