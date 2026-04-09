class Solution(object):
    def maximizeXor(self, nums, queries):
        nums.sort()
        offline, res, trie, flag = [], [-1] * len(queries), {}, False
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
                flag = True
                insert(nums[i])
                i += 1
            if flag:
                val = getMax(x)
                res[ind] = val
            else:
                res[ind] = -1
        return res


print(Solution().maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]))

