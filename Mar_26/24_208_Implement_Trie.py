class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = word

    def search(self, word):
        curr = self.trie
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        if '*' in curr:
            return True
        return False

    def startsWith(self, prefix):