import string
from collections import deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        que, used, level, ans = deque([[beginWord]]), [beginWord], 0, []
        while que:
            seq = que.popleft()
            if len(seq) > level:
                level += 1
                for word in used:
                    if word in wordList:
                        wordList.remove(word)
                used.clear()
            last = seq[-1]
            if last == endWord:
                ans.append(seq)
                while que:
                    val = que.popleft()
                    if val[-1] == endWord:
                        ans.append(val)
                return ans
            last = list(last)
            for i in range(len(last)):
                original = last[i]
                for char in string.ascii_lowercase:
                    last[i] = char
                    new_word = ''.join(last)
                    if new_word in wordList:
                        seq.append(new_word)
                        que.append(seq.copy())
                        used.append(new_word)
                        seq.pop()
                    last[i] = original
        return ans

print(Solution().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))