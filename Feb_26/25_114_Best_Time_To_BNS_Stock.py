class Solution(object):
    def maxProfit(self, prices):
        best, buy = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] - buy > best:
                best = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]
        return best


print(Solution().maxProfit(prices = [7,1,5,3,6,4]))