class Solution(object):
    def trap(self, height):
        n, water = len(height), 0
        left_max, right_max = [0] * n, [0] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])
            right_max[n - i - 1] = max(right_max[n - i], height[n - i])
        for i in range(1, n - 1):
            val = min(left_max[i], right_max[i])
            water += max(0, val - height[i])
        return water

print(Solution().trap(height = [4,2,0,3,2,5]))