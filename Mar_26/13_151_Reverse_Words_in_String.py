class Solution(object):
    def reverseWords(self, s):
        words, i, res = [], 0, ''
        while s[i] == ' ':
            i += 1
        while i < len(s):
            letter = ''
            while i < len(s) and s[i] != ' ':
                letter += s[i]
                i += 1
            words.append(letter)
            while i < len(s) and s[i] == ' ':
                i += 1
        for word in range(len(words) - 1, -1, -1):
            res += words[word]
            if word != 0:
                res += ' '
        return res
    
print(Solution().reverseWords(s = "  hello world  "))