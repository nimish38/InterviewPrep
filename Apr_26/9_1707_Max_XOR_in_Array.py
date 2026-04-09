class Solution(object):
    def maximizeXor(self, nums, queries):
        nums.sort()
        offline, res, trie = [], [-1] * len(queries), {}
        for i in range(len(queries)):
            x, m = queries[i]
            offline.append([m, x, i])
        offline.sort(key=lambda r: r[0])

        def insert(num):
            curr = trie
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in curr:
                    curr[bit] = {}
                curr = curr[bit]

        def getMax(num):
            curr, maxNum = trie, 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opp = 1 - bit
                if opp in curr:
                    curr = curr[opp]
                    maxNum = maxNum | (1 << i)
                else:
                    curr = curr[bit]
            return maxNum

        i = 0
        for m, x, ind in offline:
            while i < len(nums) and nums[i] <= m:
                insert(nums[i])
            val = getMax(x)
            if val == 0:
                res[ind] = -1
            else:
                res[ind] = val
        return res


print(Solution().maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]))

