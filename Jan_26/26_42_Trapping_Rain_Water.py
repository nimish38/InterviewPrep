class Solution(object):
    def trap(self, height):
        n, water = len(height), 0
        left, right, left_max, right_max = 0, n - 1, height[0], height[-1]
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water

print(Solution().trap(height = [4,2,0,3,2,5]))