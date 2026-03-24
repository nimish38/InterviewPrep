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
        curr = self.trie
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))