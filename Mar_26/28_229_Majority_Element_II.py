class Solution(object):
    def majorityElement(self, nums):
        target, top1, top2, res = len(nums) // 3, [None, 0], [None, 0], []
        for num in nums:
            if top1[0] == None:
                top1 = [num, 1]
            elif num != top1[0] and top2[0] == None:
                top2 = [num, 1]
            elif num == top1[0]:
                top1[1] += 1
            elif num == top2[0]:
                top2[1] += 1
            else:
                top2[1] -= 1
                if top2[1] == -1:
                    top2 = [num, 1]
            if top2[1] > top1[1]:
                top1, top2 = top2, top1

        top1[1], top2[1] = 0, 0
        for num in nums:
            if num == top1[0]:
                top1[1] += 1
            if num == top2[0]:
                top2[1] += 1
        if top1[1] > target:
            res.append(top1[0])
        if top2[1] > target:
            res.append(top2[0])
        return res

print(Solution().majorityElement(nums=[1, 2]))
