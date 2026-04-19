class Solution(object):
    def findMaximumXOR(self, nums):
        trie, res = {}, 0

        def insert(num):
            curr, bit = trie, -1
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in curr:
                    curr[bit] = {}
                curr = curr[bit]

        def getMax(num):
            curr, bit, val = trie, -1, 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if 1 - bit in curr:
                    curr = curr[1 - bit]
                    val = (1 << i) | val
                else:
                    curr = curr[bit]
            return val

        for _ in nums:
            insert(_)
        for _ in nums:
            res = max(res, getMax(_))
        return res

print(Solution().findMaximumXOR(nums = [3,10,5,25,2,8]))