class Solution(object):
    def numTrees(self, n):
        memo = [0] * (n + 1)
        memo[0] = memo[1] = 1
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left, right = root - 1, nodes - root
                memo[nodes] += memo[left] * memo[right]
        return memo[n]

print(Solution().numTrees(5))