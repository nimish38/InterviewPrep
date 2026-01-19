class Solution:
    def countAndSay(self, n: int) -> str:
        
        def performRLE(s):
            st = []
            for c in s:
                if not st or st[-1][1] != c:
                    st.append([1, c])
                else:
                    st[-1][1] += 1
            res = ''
            for num, char in st:
                res += str(num) + char
            return res

        if n == 1:
            return "1"
        curr = "1"
        for _ in range(n - 1):
            curr = performRLE(curr)
        return curr