class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        return ' '.join(s[::-1])
    
print(Solution().reverseWords(s = "  hello world  "))